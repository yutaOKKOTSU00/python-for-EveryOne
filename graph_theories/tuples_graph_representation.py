# CELL 1: representation graph using tuples  G = (V, E)
from collections import namedtuple
Graph = namedtuple("Graph", ["nodes", "edges"])

nodes = ["A", "B", "C", "D"]
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("A", "D"),
    ("B", "D"),
    ("C", "D")]

G = Graph(nodes, edges)