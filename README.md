# Core Graph Algorithms

A Python library for fundamental graph algorithms and operations. This library is built from scratch using strictly standard Python libraries.

## Features

*   **Graph Data Structure (`src/graph_core.py`)**: A foundational `Graph` class implemented using an adjacency list.
*   **Graph Traversal & Pathfinding (`src/graph_core.py`)**: Breadth-First Search (BFS) with $O(V + E)$ time complexity and Dijkstra's algorithm for shortest paths with $O((V + E) \log V)$ time complexity.
*   **Combinatorics (`src/combinatorics.py`)**: Standalone module for computing factorials ($O(n)$ time complexity, optimized with caching), permutations, and combinations.
*   **Stable Matching (`src/matching.py`)**: An implementation of the Gale-Shapley Stable Marriage algorithm.
*   **Centrality Measures (`src/centrality.py`)**: A normalized degree centrality calculator for graph nodes.

## Directory Structure

```text
.
├── README.md
├── examples/
│   └── market_simulation.py
├── src/
│   ├── __init__.py
│   ├── centrality.py
│   ├── combinatorics.py
│   ├── graph_core.py
│   └── matching.py
└── tests/
    ├── __init__.py
    ├── test_combinatorics.py
    └── test_graph.py
```

## Requirements

*   Python 3.7+
*   No external dependencies required (uses standard library only).

## Installation

You can clone this repository and use the code directly:

```bash
git clone <repository_url>
cd <repository_directory>
```

## Usage Examples

### 1. Basic Graph and Centrality

```python
from src.graph_core import Graph
from src.centrality import calculate_degree_centrality

# Create a graph
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("C", "D")

# Calculate normalized degree centrality
centrality = calculate_degree_centrality(g)
print(centrality)
# Output: {'A': 0.666..., 'B': 0.333..., 'C': 0.666..., 'D': 0.333...}
```

### 2. Graph Traversal and Pathfinding

```python
from src.graph_core import Graph

# Create a graph with weights
g = Graph()
g.add_edge("A", "B", weight=1.0)
g.add_edge("B", "C", weight=2.0)
g.add_edge("A", "C", weight=4.0)

# Perform Breadth-First Search
traversal = g.bfs("A")
print(traversal)
# Output: ['A', 'B', 'C']

# Calculate shortest paths
distances = g.dijkstra("A")
print(distances)
# Output: {'A': 0.0, 'B': 1.0, 'C': 3.0}
```

### 3. Combinatorics

```python
from src.combinatorics import factorial, permutations, combinations

# Calculate factorial
print(factorial(5)) # Output: 120

# Calculate permutations P(5, 3)
print(permutations(5, 3)) # Output: 60

# Calculate combinations C(5, 3)
print(combinations(5, 3)) # Output: 10
```

### 4. Stable Matching Simulation

You can run the provided example script to simulate a stable matching between two groups (e.g., Workers and Firms):

```bash
python examples/market_simulation.py
```

## Running Tests

To run the unit tests for this library, execute the following command from the root of the repository:

```bash
python -m unittest discover tests/
```
