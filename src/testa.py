import networkx as nx 

def A1():
    G = nx.florentine_families_graph()
    return (nx.diameter(G), nx.density(G), nx.average_clustering(G))

def A2():
    G = nx.davis_southern_women_graph()
    degree_sequence = sorted([d for n, d in G.degree()])
    degree_count = {x:degree_sequence.count(x) for x in range(max(degree_sequence)+1)}
    return (list(degree_count.keys()), list(degree_count.values()))



print(A1())
print(A2())



