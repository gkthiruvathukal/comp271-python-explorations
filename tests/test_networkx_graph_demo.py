import unittest
from data_structures.networkx_graph_demo import NetworkXGraphDemo

class TestNetworkXGraphDemo(unittest.TestCase):

    def setUp(self):
        self.graph = NetworkXGraphDemo()
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_vertex('D')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'D')

    def test_display(self):
        self.assertEqual(self.graph.display(), {'A': {'B': {}, 'C': {}}, 'B': {'A': {}, 'D': {}}, 'C': {'A': {}}, 'D': {'B': {}}})

    def test_shortest_path(self):
        self.assertEqual(self.graph.shortest_path('A', 'D'), ['A', 'B', 'D'])

    def test_connected_components(self):
        self.assertEqual(self.graph.connected_components(), [{'A', 'B', 'C', 'D'}])

if __name__ == '__main__':
    unittest.main()
    