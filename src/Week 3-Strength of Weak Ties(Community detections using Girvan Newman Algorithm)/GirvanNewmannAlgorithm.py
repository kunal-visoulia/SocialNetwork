'''based on edge betweeness:intercomm edges have high value of betweenes, means, a number of shortest paths pass through these edges.If we  find the edge betweeness of these edges and keep removing them we tend to get the community structure'''
import networkx as nx
def edge_to_remove(G):
    dict1=nx.edge_betweenness_centrality(G)
    #order is not a thing of dictionary, no association with index
    list_of_tuples=dict1.items()
    list_of_tuples.sort(key=lambda x:x[1],reverse=True)
    # how we sort a list of tuples based on second vale of the tuples in the list
    return list_of_tuples[0][0] #return in form(a,b)

def gir(G):
    c=nx.connected_component_subgraphs(G)
    
    #returns the list ofconnected components of the graph as subgraphs
    #if c=1 graph is connected else not 
    l=len(list(c))
    print('no. of connected components=',l)
    
    while(l==1):#keep doing this till the graph is connected
        G.remove_edge(*edge_to_remove(G))#form=((a,b)),so *to get the content of tuple and not the tuple
        c=nx.connected_component_subgraphs(G)
        l=len(c)
        print('no. of connected components=',l)

    return c
c=[]
G=nx.barbell_graph(6,0)
c=gir(G)
for i in c:
    print(i.nodes())
    print('.............')
    
    
    