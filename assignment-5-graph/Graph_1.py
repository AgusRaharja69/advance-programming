import networkx as nx
import matplotlib.pyplot as plt

Node = nx.Graph()

#adding a list of edges
Node.add_edges_from([(1, 4), (1, 7), (4, 2), (2, 7), (2, 0), 
(0, 7), (0, 5), (0, 6), (5, 7), (5, 6), (6, 7), (6, 3), (5, 3)])

#Show the graph
nx.draw(Node, with_labels=True)
fig = plt.gcf()
plt.show()
fig.savefig('Graph_1.png')