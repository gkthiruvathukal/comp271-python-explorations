import networkx as nx

class NetworkXGraphDemo:
    def __init__(self):
        self.graph = nx.Graph()

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        self.graph.add_node(vertex)

    def add_edge(self, vertex1, vertex2):
        """Add an edge between vertex1 and vertex2."""
        self.graph.add_edge(vertex1, vertex2)

    def display(self):
        """Display the adjacency list of the graph."""
        return dict(self.graph.adjacency())

    def shortest_path(self, start, end):
        """Find the shortest path between two vertices."""
        return nx.shortest_path(self.graph, start, end)

    def connected_components(self):
        """Find all connected components in the graph."""
        return list(nx.connected_components(self.graph))
    