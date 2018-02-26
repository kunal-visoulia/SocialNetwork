#prefix
import networkx as nx

#"Enter m1 and m2 seperated by the space: "
m1, m2 = map(int, raw_input().split())
G = nx.barbell_graph(m1, m2)
def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G) 
    list_of_tuples = dict1.items()
    list_of_tuples.sort(key = lambda x:x[1], reverse = True) #Descending order
    d=list_of_tuples[0][0]
    return d #(a, b) #edge with max edge betweenness
    
list2 =[]
list2.append(edge_to_remove(G))
def girvan(G):
    # Returns connected components as subgrahs
    c = list(nx.connected_component_subgraphs(G))
    l = len(c)
    while l == 1:
        x=G.remove_edge(*edge_to_remove(G)) # ((a, b)) -> (a, b)
        c = list(nx.connected_component_subgraphs(G))
        l = len(c)
    return c

G = nx.barbell_graph(m1,m2)
c = girvan(G)

list1 = (list(i.nodes()) for i in c)
print list(list1)
print (list2)