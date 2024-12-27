# CELL 2:  adjacency list : dictionary in wich each node(vertex) is a key who's values are nodes connected with it
from tuples_graph_representation import G

def adjacency_dict(graph):
    # return the adjacency list representation of the graph
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)
    return adj 