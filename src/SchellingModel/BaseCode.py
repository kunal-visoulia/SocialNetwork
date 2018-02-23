import networkx as nx
import matplotlib.pyplot as plt
import random as rn

N=10
G=nx.grid_2d_graph(N,N)
#actual grid represenation
pos=dict((n,n) for n in G.nodes())
#nx.draw(G,pos)
#plt.show()

#assign node coords as node label
labels=dict(((i,j),i*10+j) for i,j in G.nodes())
#nx.draw(G,pos,with_labels=True)
#plt.show()
#nx.draw(G,pos,with_labels=False)
#nx.draw_networkx_labels(G,pos,labels=labels)
#plt.show()

#inner nodes should have 8 neighbors but has only 6 because of no edges between diagnol nodes
#nx.draw(G,pos,with_labels=True)
#plt.show()
#nodes (i,j) needs to be connected node (i+1,j+1)
for (u,v) in G.nodes():
    if(u+1<=N-1)and(v+1<=N-1):
        G.add_edge((u,v),(u+1,v+1))
    if(u+1<=N-1)and(v-1>=0):
        G.add_edge((u,v),(u+1,v-1))
        
nx.draw(G,pos,with_labels=False)
nx.draw_networkx_labels(G,pos,labels=labels)
#plt.show()

#adding people to these nodes type0:empty node type1:people of type 1 type2:people of type 2
for n in G.nodes():
    G.node[n]['type']=rn.randint(0,2)
type1_node_list=[n for (n,d) in G.nodes(data=True) if d['type']==1]
#data =true so as G.nodes()gives list of nodes as well as value of attribute of the nodes, 
#we get (n,d) where n is the node and d is the dictionary containg the attribute and its value(type)
type2_node_list=[n for (n,d) in G.nodes(data=True) if d['type']==2]
empty_cells=[n for (n,d) in G.nodes(data=True) if d['type']==10]

def display_graph(G):
    nodes_g=nx.draw_networkx_nodes(G,pos,node_color='green',nodelist=type1_node_list)
    nodes_r=nx.draw_networkx_nodes(G,pos,node_color='red',nodelist=type2_node_list)
    nodes_w=nx.draw_networkx_nodes(G,pos,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G,pos,labels=labels)
    plt.show()
    
#display_graph(G)

def get_boundary_nodes(G):    
    #nodes with u=0, v=0, u=N-1 or v=N-1 are boundary nodes
    boundary_nodes_list=[]
    for (u,v) in G.nodes():
        if u==0 or v==0 or u==N-1 or v==N-1:
            boundary_nodes_list.append((u,v))
    return boundary_nodes_list
            
boundary_nodes_list=get_boundary_nodes(G)
internal_nodes_list=list(set(G.nodes())-set(boundary_nodes_list))
print boundary_nodes_list
print internal_nodes_list