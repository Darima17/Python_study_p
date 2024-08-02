import json
import logging
import argparse
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
from neo4j import GraphDatabase


WIKI_URL: str = "https://en.wikipedia.org"
DB_NAME: str = "cachewiki"
GRAPH_JSON_FILE = "graph.json"

graph: dict = {}
page_count: int = 0


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))


    def close(self):
        if self.driver is not None:
            self.driver.close()


    def query(self, query, parameters=None, db_name=None):
        assert self.driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.driver.session(database=db_name) if db_name is not None else self.driver.session()
            response = list(session.run(query, parameters))
        except Exception as e:
            logging.error("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


def save_graph_in_neo4j(graph, conn):
    conn.query(f"CREATE OR REPLACE DATABASE {DB_NAME}")
    conn.query(f"START DATABASE {DB_NAME} WAIT 30 SECONDS")

    for title, node in graph.items():
        link = node["link"]
        conn.query(
            "MERGE (a:Article {title: $title, link: $link})",
            parameters={"title": title, "link": link},
            db_name=DB_NAME
        )
        
        for rel in node["relationships"]:
            rel_title = rel["title"]
            rel_link = rel["link"]
            
            conn.query(
                "MERGE (b:Article {title: $title, link: $link})",
                parameters={"title": rel_title, "link": rel_link},
                db_name=DB_NAME
            )
            conn.query(
                """
                MATCH (a:Article {title: $src_title})
                MATCH (b:Article {title: $dst_title})
                MERGE (a)-[:RELATED_TO]->(b)
                """,
                parameters={"src_title": title, "dst_title": rel_title},
                db_name=DB_NAME
            )


def save_graph_in_json_file(graph: dict):
    try:
        with open(GRAPH_JSON_FILE, 'w', encoding='utf-8') as file:
            json.dump(graph, file, indent=4)
    except Exception as e:
        logging.error("Error during save json file!")


def load_wiki_html(page_link: str) -> bytes:
    url = WIKI_URL + page_link
    # logging.info(url)
    fp = None
    try:
        fp = urllib.request.urlopen(url)
        html_bytes = fp.read()
        fp.close()
    except urllib.request.HTTPError as e:
        logging.error(e)
    return html_bytes


def check_link(link: str):
    if link.startswith("/wiki/") and \
    not link.startswith("/wiki/File") and \
    not  link.startswith("/wiki/Help") and \
    not  link.startswith("/wiki/Special"):
        return True
    return False


def parse_html(html_bytes: bytes) -> list[map]:
    pages_info = []
    soup = BeautifulSoup(html_bytes, 'html.parser')

    for link in soup.find("div", {"id": "bodyContent"}).select('a[href^="/wiki/"]'):
        if check_link(link.get('href')):
            pages_info += [{'title': link.get('title'), 'link': link.get('href')}]

    see_also_tag = soup.find("span", id="See_also")
    references_tag = soup.find("span", id="References")

    if see_also_tag is None:
        logging.warning("See also paragraph did not found!")

    between = False
    for item in soup.find_all():
        if item == references_tag or item.name == "h2":
            between = False

        if between is True and item.name == "ul":
            pages_info += [{'title': a['title'], 'link': a['href']}
                           for a in item.find_all("a", href=True, title=True) if check_link(a['href'])]

        if item == see_also_tag:
            between = True
    return pages_info


def add_vertex(page_info) -> bool:
    global page_count
    if page_count >= max_page_stored:
        logging.info("Max pages count was reached!")
        return False
    if page_info['title'] not in graph:
        logging.info(WIKI_URL + page_info['link'])
        graph[page_info['title']] = {'link': page_info['link'], 'relationships': []}
        page_count += 1
    return True


def add_relationships(page_title, pages_info) -> bool:
    for page in pages_info:
        if add_vertex(page) is False:
            return False
        graph[page_title]['relationships'].append(page)
    return True


def handle_see_also_pages(see_also_pages_info, depth: int = 3) -> bool:
    try:
        for page in see_also_pages_info:
            if add_vertex(page) is False:
                return False

            html_bytes = load_wiki_html(page['link'])
            pages_info = parse_html(html_bytes)

            if add_relationships(page['title'], pages_info) is False:
                return False

        if depth <= 0:
            logging.info("Max depth was reached!")
            return False

        for page in see_also_pages_info:
            pages_info = graph[page['title']]['relationships']
            if handle_see_also_pages(pages_info, depth=depth - 1) is False:
                return False
        return True
    except Exception as e:
        logging.error(e)
        return False


def parse_args():
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--article", default="Michelangelo", help="Require wiki page", type=str)
    parser.add_argument("-d", "--max-depth", default=3, help="Require depth of parsing", type=int)
    parser.add_argument("-l", "--max-page-stored", default=1000, help="Require max links count to be saved in json", type=int)
    args = parser.parse_args()
    return args


def main() -> None:
    global page_title, max_page_stored
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    args = parse_args()

    page_title = args.article
    max_page_stored = args.max_page_stored
    max_depth = args.max_depth

    link = "/wiki/" + quote(page_title)

    if add_vertex({'title': page_title, 'link': link}):

        html_bytes = load_wiki_html(link)
        see_also_pages_info = parse_html(html_bytes)
        if len(see_also_pages_info) < 20:
            logging.info("Pages links less than 20, please select another page!")
            exit(0)

        if add_relationships(page_title, see_also_pages_info):
            handle_see_also_pages(see_also_pages_info, max_depth)
        else:
            logging.error("Error during add relationships for main page!")
    else:
        logging.error("Error during add main page vertex!")

    conn = Neo4jConnection(uri="bolt://localhost:7687", user="neo4j", password="12345678")
    save_graph_in_neo4j(graph, conn)
    save_graph_in_json_file(graph)


if __name__ == "__main__":
    main()
