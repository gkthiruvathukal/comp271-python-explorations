import unittest
from data_structures.graph_demo import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_vertex('D')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'D')

    def test_display(self):
        self.assertEqual(self.graph.display(), {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A'], 'D': ['B']})

    def test_bfs(self):
        self.assertEqual(self.graph.bfs('A'), ['A', 'B', 'C', 'D'])

    def test_dfs(self):
        self.assertEqual(self.graph.dfs('A'), ['A', 'B', 'D', 'C'])

if __name__ == '__main__':
    unittest.main()
    