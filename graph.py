# coding=utf-8
"""
参考官网教程：
Tutorial — NetworkX 2.3 documentation
https://networkx.github.io/documentation/stable/tutorial.html#
"""
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
# H = nx.path_graph(10)
# G.add_nodes_from(H)
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*
G.add_edges_from([(1, 2), (1, 3)])
# G.add_edges_from(H.edges)
print(G.nodes, G.edges)
print(G.adj, G.degree[1])
print([i for i in G.neighbors(1)])
# G.clear()

# G.add_edges_from([(1, 2), (1, 3)])
# G.add_node(1)
# G.add_edge(1, 2)
# G.add_node("spam")
# G.add_nodes_from("spam")
# G.add_edge(3, 'm')
# G.remove_node(2)
# G.remove_nodes_from("spam")
# G.remove_edge(1, 3)
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# # G[1][3]['color'] = "blue"
# # G.edges[1, 2]['color'] = "red"
# G.remove_node('spam')
#
# # H = nx.DiGraph(G)
# # edgelist = [(0, 1), (1, 2), (2, 3)]
# # H = nx.Graph(edgelist)
# # print(H.edges, H.nodes, H.number_of_nodes(), H.number_of_edges(), H.graph)
# print(G.nodes, G.edges, G.number_of_edges(), G.number_of_nodes() )
# print(G.adj, G.degree)
G = nx.petersen_graph()
plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()