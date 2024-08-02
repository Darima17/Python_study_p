import os
import json
import networkx as nx
import matplotlib.pyplot as plt
import logging
from pyvis.network import Network

WIKI_FILE = "../ex00/graph.json"


def render_graph(graph_file) -> None:
    try:
        with open(graph_file) as f:
            data = json.load(f)
    except Exception as e:
        logging.error(f"Error during openning the file {graph_file}")
        exit(1)

    G = nx.DiGraph()
    # add nodes
    for node in data.values():
        G.add_node(node["link"], label=node["link"], size=len(node["relationships"]))

    # add edges
    for node in data.values():
        for relationship in node["relationships"]:
            G.add_edge(node["link"], relationship["link"], weight=1)

    in_degrees = dict(G.in_degree())
    node_sizes = [10 + 10 * in_degrees.get(node, 0) for node in G.nodes()]

    # save the graph in png format
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color="lightgreen", edge_color="gray", width=0.5, font_size=5, font_family="sans-serif")
    plt.savefig("wiki_graph.png", dpi=max(300, plt.gcf().dpi), bbox_inches="tight")
    # save the graph in interactive html format
    n = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True, cdn_resources='in_line')
    n.from_nx(G)
    n.show("wiki_graph.html")


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    try:
        WIKI_FILE = os.environ["WIKI_FILE"]
    except Exception as e:
        logging.error("Env Variable 'WIKI_FILE' does not set")
        exit(1)

    render_graph(WIKI_FILE)


if __name__ == "__main__":
    main()
