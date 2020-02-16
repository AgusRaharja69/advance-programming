import networkx as nx
import matplotlib.pyplot as plt
Node = nx.Graph()
         
Node.add_edges_from([(7, 11) ,
            (7, 8) ,
            (7, 6) ,
            (8, 11) ,
            (8, 6) ,
            (8, 10) ,
            (10, 9) ,
            (10, 6) ,
            (11, 6)])
            
Node.add_edges_from([(6, 2),
            (2, 5) ,
            (2, 1) ,
            (5, 3) ,
            (5, 0) ,
            (3, 1) ,
            (1, 0) ,
            (1, 4) ,
            (0, 4)])

pos = nx.spring_layout(Node)
nx.edge_betweenness_centrality(Node, k=None, normalized=True)
nx.draw(Node, pos, with_labels=True, edgelist=[(6,2)],width=8, alpha=0.5, edge_color='r')
nx.draw(Node, pos, with_labels=True)
fig = plt.gcf()
plt.show()
fig.savefig('Graph_2.png')


