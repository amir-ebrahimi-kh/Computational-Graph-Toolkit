from typing import Dict, List, Tuple, TypeVar, Generic

T = TypeVar('T')

class Graph(Generic[T]):
    """A simple graph representation using an adjacency list.

    Attributes:
        _adjacency_list: A dictionary mapping nodes to a list of their adjacent nodes.
    """

    def __init__(self) -> None:
        """Initializes an empty graph."""
        self._adjacency_list: Dict[T, List[T]] = {}
        self._weights: Dict[Tuple[T, T], float] = {}

    def add_node(self, node: T) -> None:
        """Adds a node to the graph if it doesn't already exist.

        Args:
            node: The node to be added to the graph. Can be of any hashable type.
        """
        if node not in self._adjacency_list:
            self._adjacency_list[node] = []

    def add_edge(self, u: T, v: T, directed: bool = False, weight: float = 1.0) -> None:
        """Adds an edge between two nodes in the graph.

        If the nodes do not exist, they will be added automatically.

        Args:
            u: The source node of the edge.
            v: The destination node of the edge.
            directed: A boolean indicating whether the edge is directed (True)
                      or undirected (False). Defaults to False.
            weight: The weight of the edge. Defaults to 1.0.
        """
        self.add_node(u)
        self.add_node(v)

        self._adjacency_list[u].append(v)
        self._weights[(u, v)] = weight

        if not directed:
            self._adjacency_list[v].append(u)
            self._weights[(v, u)] = weight

    def get_graph(self) -> Dict[T, List[T]]:
        """Returns the adjacency list representation of the graph.

        Returns:
            A dictionary where keys are nodes and values are lists of adjacent nodes.
        """
        return self._adjacency_list

    def bfs(self, start_node: T) -> List[T]:
        """Performs Breadth-First Search traversal starting from the given node.

        Args:
            start_node: The node to start the traversal from.

        Returns:
            A list of nodes in the order they were visited.
        """
        import collections
        if start_node not in self._adjacency_list:
            return []

        visited = {start_node}
        queue = collections.deque([start_node])
        traversal_order = []

        while queue:
            current = queue.popleft()
            traversal_order.append(current)

            for neighbor in self._adjacency_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dijkstra(self, start_node: T) -> Dict[T, float]:
        """Computes the shortest paths from the start node to all other reachable nodes
        using Dijkstra's algorithm.

        Args:
            start_node: The node to start pathfinding from.

        Returns:
            A dictionary mapping each reachable node to its shortest path distance
            from the start node.
        """
        import heapq

        distances = {node: float('inf') for node in self._adjacency_list}
        if start_node not in distances:
            return {}

        distances[start_node] = 0.0
        priority_queue = [(0.0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self._adjacency_list.get(current_node, []):
                weight = self._weights.get((current_node, neighbor), 1.0)
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return {node: dist for node, dist in distances.items() if dist != float('inf')}