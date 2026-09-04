import unittest
from src.graph_core import Graph
from src.matching import stable_matching
from src.centrality import calculate_degree_centrality

class TestGraphCore(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        self.graph.add_node("A")
        self.assertIn("A", self.graph.get_graph())
        self.assertEqual(self.graph.get_graph()["A"], [])

    def test_add_edge_undirected(self):
        self.graph.add_edge("A", "B")
        adj_list = self.graph.get_graph()
        self.assertIn("A", adj_list)
        self.assertIn("B", adj_list)
        self.assertIn("B", adj_list["A"])
        self.assertIn("A", adj_list["B"])

    def test_add_edge_directed(self):
        self.graph.add_edge("C", "D", directed=True)
        adj_list = self.graph.get_graph()
        self.assertIn("C", adj_list)
        self.assertIn("D", adj_list)
        self.assertIn("D", adj_list["C"])
        self.assertNotIn("C", adj_list["D"])

class TestMatching(unittest.TestCase):
    def test_stable_matching(self):
        group1_prefs = {
            'A': ['X', 'Y', 'Z'],
            'B': ['Y', 'X', 'Z'],
            'C': ['X', 'Y', 'Z']
        }
        group2_prefs = {
            'X': ['B', 'A', 'C'],
            'Y': ['A', 'B', 'C'],
            'Z': ['A', 'B', 'C']
        }

        matches = stable_matching(group1_prefs, group2_prefs)

        self.assertEqual(len(matches), 3)
        self.assertEqual(matches['A'], 'X')
        self.assertEqual(matches['B'], 'Y')
        self.assertEqual(matches['C'], 'Z')

class TestCentrality(unittest.TestCase):
    def test_degree_centrality_empty(self):
        g = Graph()
        centrality = calculate_degree_centrality(g)
        self.assertEqual(centrality, {})

    def test_degree_centrality_single_node(self):
        g = Graph()
        g.add_node("A")
        centrality = calculate_degree_centrality(g)
        self.assertEqual(centrality, {"A": 0.0})

    def test_degree_centrality_star_graph(self):
        g = Graph()
        # A is center, B C D are leaves
        g.add_edge("A", "B")
        g.add_edge("A", "C")
        g.add_edge("A", "D")

        centrality = calculate_degree_centrality(g)

        self.assertEqual(centrality["A"], 1.0) # connected to all 3 other nodes
        self.assertAlmostEqual(centrality["B"], 1/3)
        self.assertAlmostEqual(centrality["C"], 1/3)
        self.assertAlmostEqual(centrality["D"], 1/3)

if __name__ == '__main__':
    unittest.main()
