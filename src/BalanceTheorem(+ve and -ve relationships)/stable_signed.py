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
    return unstable
unstable=count_unstable(all_signs)
unstable_track=[unstable]
#5. do it till there are unstable triangles in the graph(5.1 to 5.3)

#5.1 choose an unstable triangle
def move_a_tri_to_stable(G,triangles_list,all_signs):
    found_unstable=False
    while(found_unstable==False):
        index=rn.randint(0,len(triangles_list)-1)
        #check for triangle at position=index , unstable or stable
        if all_signs[index].count('+')==2 or all_signs[index].count('+')==0:
            found_unstable=True
        else:
            continue
    #5.2 make the triangle stable
    #there are 3 possible corresponding stable states for an unstable state(there are 2 possible unstable states)
    #for #+=2, inversion of sign  of any one side leads to a stable state
    #for #+=0, -ve sign of any one side to =ve leads to a stable sate
    r=rn.randint(1,3)#for chossing one out of 3 possible states
    
    if all_signs[index].count('+')==2:
        if r==1:
            if G[triangles_list[index][0]][triangles_list[index][1]]['sign']=='+':
                G[triangles_list[index][0]][triangles_list[index][1]]['sign']='-'
            elif G[triangles_list[index][0]][triangles_list[index][1]]['sign']=='-':
                G[triangles_list[index][0]][triangles_list[index][1]]['sign']='+'
                
        elif r==2:
            if G[triangles_list[index][1]][triangles_list[index][2]]['sign']=='+':
                G[triangles_list[index][1]][triangles_list[index][2]]['sign']='-'
            elif G[triangles_list[index][1]][triangles_list[index][2]]['sign']=='-':
                G[triangles_list[index][1]][triangles_list[index][2]]['sign']='+'
         
        elif r==3:
            if G[triangles_list[index][0]][triangles_list[index][2]]['sign']=='+':
                G[triangles_list[index][0]][triangles_list[index][2]]['sign']='-'
            elif G[triangles_list[index][0]][triangles_list[index][2]]['sign']=='-':
                G[triangles_list[index][0]][triangles_list[index][2]]['sign']='+'           
    
    if all_signs[index].count('+')==0:
        if r==1:
            G[triangles_list[index][0]][triangles_list[index][1]]['sign']='+'
                
        elif r==2:
            G[triangles_list[index][1]][triangles_list[index][2]]['sign']='+'
         
        elif r==3:
            G[triangles_list[index][0]][triangles_list[index][2]]['sign']='+'  
                  
    return G
    
while(unstable!=0):
    G=move_a_tri_to_stable(G,triangles_list,all_signs)
    #after a triangle is made stable and graph is updated, adjacent triangle may get unstable 
    # and thus signs of the triangles need to be reevaluated
    #we can choose to reevaluate signs of all triangles(chosen way) or only adjacent triangles
    all_signs=get_signs_of_triangles(triangles_list,G)
    #5.3 update unstable
    unstable=count_unstable(all_signs)
    unstable_track.append(unstable)

#how the number of unstable triangles change when we move one unstable triangle to
#a stable state
raw_input()    
plt.bar([i for i in range(len(unstable_track))],unstable_track)
plt.xlabel('no of iterations of while loop')
plt.ylabel('no. of unstable triangles')
plt.show()
    
    
    





