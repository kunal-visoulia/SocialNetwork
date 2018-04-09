import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
G.add_nodes_from(range(0,50))
nx.draw(G)
plt.show()
