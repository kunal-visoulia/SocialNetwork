import networkx as nx


G=nx.erdos_renyi_graph(10,0.5)
nx.write_gml(G,'random_graph.gml')

