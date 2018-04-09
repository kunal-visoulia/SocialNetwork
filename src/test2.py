import networkx as nx
import random

edge_list = [(1, 2), (1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5), (5, 6), (7, 8), (7, 10), (8, 9), (9, 10)]
# create G2 and Gc using edge_list

n_edges_added_for_weak_connectedness = 0
n_edges_added_for_strong_connectedness = 0
G2=nx.graph()
G2.add_node(range(1,11))
G2.add_edge(x for x in edge_list)
while(nx.is_strongly_connected(G2) == False):
    u = random.choice(list(G2.nodes()))
    v = random.choice(list(G2.nodes()))
    if(u != v):
        if(nx.is_weakly_connected(G2) == False):
            G2.add_edge(u, v)
            n_edges_added_for_strong_connectedness += 1
            n_edges_added_for_weak_connectedness += 1
        else:
            G2.add_edge(u, v)
            n_edges_added_for_strong_connectedness += 1
        
Gc=G2.copy()