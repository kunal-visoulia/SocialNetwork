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

#getting neoghbours of internal and boundary nodes
def get_neigh_internal(u,v):
    return [(u-1,v),(u+1,v),(u,v-1),(u,v+1)(u-1,v-1),(u+1,v-1),(u-1,v+1),(u+1,v+1)]

def get_neigh_boundary(u,v):
    global N
    if u==0and v==0:
        return [(0,1),(1,1),(1,0)]
    elif u==N-1 and v==N-1:
        return [(N-2,N-2),(N-1,N-2),(N-2,N-1)]
    elif u==N-1 and v==0:
        return [(u-1,v),(u,v+1),(u-1,v+1)]
    elif u==0 and v==N-1:
        return [(u+1,v),(u+1,v-1),(u,v-1)]
    elif u==0:
        return [(u,v-1),(u,v+1),(u+1,v),(u+1,v-1),(u+1,v+1)]
    elif u==N-1:
        return [(u-1,v),(u,v-1),(u,v+1),(u-1,v+1),(u-1,v-1)]
    elif v==N-1:
        return [(u,v-1),(u-1,v),(u+1,v),(u-1,v-1),(u+1,v-1)]
    elif v==0:
        return [(u-1,v),(u+1,v),(u,v+1),(u-1,v+1),(u+1,v+1)]
    
def get_unsatisfied_nodes_list(G,boundary_nodes_list,internal_nodes_list):
    unsatisfied_nodes_list=[]
    t=3
    for u,v in G.nodes():
        type_of_this_node=G.node[(u,v)]['type']
        if type_of_this_node==0:
            continue
        else:
            similar_nodes=0
            if (u,v) in internal_nodes_list:
                neigh=get_neigh_internal(u, v)
            elif (u,v) in boundary_nodes_list:
                neigh=get_neigh_boundary(u, v)
            
            for each in neigh:
                if G.node[each]['type']==type_of_this_node:
                    similar_nodes+=1
            if similar_nodes<=t:
                unsatisfied_nodes_list.append((u,v))
                
    return unsatisfied_nodes_list

unsatisfied_nodes_list=get_unsatisfied_nodes_list(G, boundary_nodes_list, internal_nodes_list)
 
    















