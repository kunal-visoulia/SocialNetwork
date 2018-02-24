import networkx as nx
import matplotlib.pyplot as plt
import random as rn
import itertools 
from networkx.algorithms.bipartite.basic import color

#1. create a graph with n nodes, where nodes are countries
G=nx.Graph()
n=5
G.add_nodes_from([i for i in range(1,n+1)])
mapping={1:'USA',2:'INDIA',3:'CHINA',4:'JAPAN',5:'AUSTRIA',6:'AFRICA'}
G=nx.relabel_nodes(G,mapping)

#2. MAKE GRAPH COMPLETE AND ADD WIEGHTS [+,-] RANDOMLY
signs=['+','-']
for i in G.nodes():
    for j in G.nodes():
        if i!=j:
            G.add_edge(i,j,sign=rn.choice(signs))

#3. display the network
edge_labels=nx.get_edge_attributes(G,'sign')#to prevent displaying weights as 'sign=+' or 'sign=-'
pos=nx.circular_layout(G)
nx.draw(G,pos,node_size=5000,with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size=20,font_color='red')
plt.show()

#4.1 Get  list of all the triangles in the network
nodes=G.nodes()
triangles_list=[list(x) for x in itertools.combinations(nodes,3)]
#a list of lists containing 3 nodes that form a triangle

#4.2 store the sign details of all the triangles
def get_signs_of_triangles(triangles_list,G):
    all_signs=[]
    for i in range(len(triangles_list)):
        temp=[]
        #to get signs
        temp.append(G[triangles_list[i][0]][triangles_list[i][1]]['sign']) 
        temp.append(G[triangles_list[i][1]][triangles_list[i][2]]['sign']) 
        temp.append(G[triangles_list[i][2]][triangles_list[i][0]]['sign']) 
        all_signs.append(temp)
    return all_signs
    
all_signs=get_signs_of_triangles(triangles_list,G)
#list of lists that contains sign detials of a triangle

#4.3 count no. of unstable triangles
def count_unstable(all_signs):
    unstable=0
    stable=0
    for i in range(len(all_signs)):
        if all_signs[i].count('+')==3 or all_signs[i].count('+')==1:
             stable+=1
        elif all_signs[i].count('+')==2 or all_signs[i].count('+')==0:
            unstable+=1
    print ('Number of stable triangles out of ',stable+unstable,' are ',stable)
    print ('Number of unstable triangles out of ',stable+unstable,' are ',unstable)

unstable=count_unstable(all_signs)