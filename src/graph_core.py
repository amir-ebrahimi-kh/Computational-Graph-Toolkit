from typing import Dict, List, TypeVar, Generic

T = TypeVar('T')

class Graph(Generic[T]):
    """A simple graph representation using an adjacency list.

    Attributes:
        _adjacency_list: A dictionary mapping nodes to a list of their adjacent nodes.
    """

    def __init__(self) -> None:
        """Initializes an empty graph."""
        self._adjacency_list: Dict[T, List[T]] = {}

    def add_node(self, node: T) -> None:
        """Adds a node to the graph if it doesn't already exist.

        Args:
            node: The node to be added to the graph. Can be of any hashable type.
        """
        if node not in self._adjacency_list:
            self._adjacency_list[node] = []

    def add_edge(self, u: T, v: T, directed: bool = False) -> None:
        """Adds an edge between two nodes in the graph.

        If the nodes do not exist, they will be added automatically.

        Args:
            u: The source node of the edge.
            v: The destination node of the edge.
            directed: A boolean indicating whether the edge is directed (True)
                      or undirected (False). Defaults to False.
        """
        self.add_node(u)
        self.add_node(v)

        self._adjacency_list[u].append(v)

        if not directed:
            self._adjacency_list[v].append(u)

    def get_graph(self) -> Dict[T, List[T]]:
        """Returns the adjacency list representation of the graph.

        Returns:
            A dictionary where keys are nodes and values are lists of adjacent nodes.
        """
        return self._adjacency_list
