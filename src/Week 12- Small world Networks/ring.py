import networkx as nx
import matplotlib.pyplot as plt

def add_edges(G):
    list_nodes=G.nodes()
    n=G.number_of_nodes()
    #every nodes in this list is supposed to be connected to 2 nodes on right and left each
    for i in range(0,len(list_nodes)):
        #print list_nodes[i], list_nodes[i+1], list_nodes[i-1], list_nodes[i+2], list_nodes[i-2]
        #-ve indices pose no problem, but
        #when i+1 or i+2->n, we need to set this value to 0
        #                ->n+1, we need to set this to 1 
        G.add_edge(list_nodes[i],list_nodes[i-1])
        G.add_edge(list_nodes[i],list_nodes[i-2])
        target=i+1
        if target>n-1:
            target=target-n
            G.add_edge(list_nodes[i],target)
        else:
            G.add_edge(list_nodes[i],target)
        target=i+2
        if target>n-1:
            target=target-n
            G.add_edge(list_nodes[i],target)
        else:
            G.add_edge(list_nodes[i],target)
            
G=nx.Graph()
G.add_nodes_from(range(0,50))

add_edges(G)  #add ties based on homophily
for each in G.nodes():
    print each,':',
    for each1 in G.neighbors(each):
        print each1,
    print '\n'
nx.draw(G,with_labels=1)
plt.show()
