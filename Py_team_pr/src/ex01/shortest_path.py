import os
import json
import logging
import argparse


def dfs(src, dest, json_data, visited=None):
    if visited is None:
        visited = set()

    if src == dest:
        return [[src]]

    res = []
    if src not in visited:
        visited.add(src)

        node = json_data.get(src, None)

        if not node:
            return res

        for rel in node["relationships"]:
            node_res = dfs(rel["title"], dest, json_data, visited)
            for path in node_res:
                path.insert(0, src)
            res.extend(node_res)
    return res


def load_graph_from_json(path: str, non_directed = False):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            bytes = file.read()
    except FileNotFoundError as e:
        return None

    graph_in_json = json.loads(bytes)
    if non_directed is True:
        for title in graph_in_json:
            for relationship in graph_in_json[title]['relationships']:
                if title not in graph_in_json[relationship['title']]['relationships']:
                    graph_in_json[relationship['title']]['relationships'].append({'title': title, 'link': graph_in_json[title]['link']})
    return graph_in_json


def parse_args():
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", "--from", type=str, required=True, help="Start page title")
    parser.add_argument("--dest", "--to", type=str, required=True, help="End page title")
    parser.add_argument("--non-directed", action="store_true", default=False, help="If true - then graph bidirectional")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable logging of the found path")
    args = parser.parse_args()
    return args


def search_shortest_path(paths: list, verbose: bool = False):
    if len(paths) == 0:
        logging.info(f"path not found")
    else:
        shortest_path = paths[0]
        for path in paths:
            if len(path) < len(shortest_path):
                shortest_path = path

        if verbose is True:
            logging.info("'" + "' -> '".join(shortest_path) + "'")
        logging.info(len(shortest_path) - 1)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    try:
        WIKI_FILE = os.environ["WIKI_FILE"]
    except Exception as e:
        logging.error("Env Variable 'WIKI_FILE' does not set")
        exit(1)

    args = parse_args()

    src = args.src
    dest = args.dest
    non_directed = args.non_directed
    verbose = args.verbose

    graph_in_json = load_graph_from_json(WIKI_FILE, non_directed)
    if graph_in_json is None:
        logging.error("database not found")
        exit(1)

    paths: list = dfs(src, dest, graph_in_json)
    search_shortest_path(paths, verbose)


if __name__ == "__main__":
    main()
