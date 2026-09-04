from typing import Dict, TypeVar
from src.graph_core import Graph

T = TypeVar('T')

def calculate_degree_centrality(graph: Graph[T]) -> Dict[T, float]:
    """Calculates the normalized degree centrality for each node in a graph.

    Degree centrality is defined as the number of links incident upon a node.
    The normalized version divides this by the maximum possible degree (n-1),
    where n is the number of nodes in the graph.

    Args:
        graph: A Graph instance for which to calculate degree centralities.

    Returns:
        A dictionary mapping each node to its normalized degree centrality score.
        If the graph has 0 or 1 nodes, the centrality score is 0.0 for all nodes.
    """
    adj_list = graph.get_graph()
    num_nodes = len(adj_list)
    centrality: Dict[T, float] = {}

    if num_nodes <= 1:
        for node in adj_list:
            centrality[node] = 0.0
        return centrality

    max_possible_degree = num_nodes - 1

    for node, neighbors in adj_list.items():
        # Using set(neighbors) in case of multiple edges to the same node in a
        # non-simple graph, but strictly speaking, standard degree centrality
        # just uses degree. Assuming simple graph here.
        degree = len(neighbors)
        centrality[node] = degree / max_possible_degree

    return centrality
