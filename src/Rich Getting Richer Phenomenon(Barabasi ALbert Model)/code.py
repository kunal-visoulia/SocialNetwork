#Rich getting Richer pheno. also called Mathew effect or Preferential attachment
#The Main Idea:
'''We start with m0 nodes, the links between which are chosen arbitrarily, as long as each node has at least one link.
then new nodes are added one by one. '''
'''The network develops in following two steps:
1)Growth:At each timestep we add a new node with 
m(<=m0) links that connect the new node to m nodes already 
in the network
2)Preferential attachment:The probability that a link of the new node connects to node i 
depends on the degree of each node.'''

#Steps for implementation
'''
1)take n from user(total number of nodes)
2)Either take m(number of edges to be connected to the new node) from the user, or decide it based on n.
In this implementation we decide it as follows:
  i)m0 is the initial number of nodes that should have atleast one link(m<=m0).
 ii)we take m0 tobe between 2 and n/5
iii)we take m=m0 - 1
3)Add the rest n-m0 nodes.Add edges to these n-m0 nodes based on'preferential attachment'.
'''

#steps to be followed for preferential attachment
'''
#For all n-m0 nodes,repeat the following:
1)Add the node
2)To add the edges, do the following:
  i)Preprocessing
      Get the dictionary at degrees(since preferential ttachment will happen based on degree)
      Maintain a dictionary of probabilities.(The probabilities have to be assigned based on degree.Prob[i]=Deg[i[/sum of degrees of all nodes)
      Maintain a list of lists for maintaining cumulative node probabilities.(This is for choosing a node based on probabilties)
      For example, Probs=[0.2,0.3,0.5]
      then cumulative probabilities=[0.2,0.5(0.2+0.3),1.0(0.5+0.5)]
      
ii)While edges added are not equal to m:
      Choose a random number from 0 to 1.
      Whenever node has cumulative prob. more than this random number, the edge will be connected to that node, if not already added.
      For example, if r=0.4 
      Node2(0.5>0.4 and thus we stop here), will be chosen

#Main idea behind this method
more prob. a node has, more likely is to get connected to incoming node.More prob. a node has, more window it will have in the cumulative probability.
for ex, windows(window size=probability) of nodes 1,2 and 3 are respectively:0-0.2, 0.2-0.5, 0.5-1.0.
A random number is more likely to fell in a larger window.
'''

import networkx as nx
import random
import matplotlib.pyplot as plt

def display_graph(G,i,ne):
    #i=new node to be added,ne is the list of new edges added
    pos=nx.circular_layout(G)
    if i=='' and ne=='':
        new_node=[]
        rest_nodes=G.nodes()
        new_edges=[]
        rest_edges=G.edges()
    else:
        new_node=[i]
        rest_nodes=list(set(G.nodes())-set(new_node))
        new_edges=ne
        rest_edges=list(set(G.edges())-set(new_edges)-set([(b,a) for (a,b) in new_edges]))
    nx.draw_networkx_nodes(G, pos, nodelist=new_node, node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=rest_nodes, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=new_edges, edge_color='g',style='-.')
    nx.draw_networkx_edges(G, pos, edgelist=rest_edges, edge_color='r')
    plt.show()
    
def add_nodes_barabasi(G,n,m0):
    m=m0-1
    for i in range(m0+1,n+1):
        G.add_node(i)
        #add the edges one by one
        #preprocessing
        degrees=nx.degree(G)
        node_probabilities={}
        
        for each in G.nodes():
            node_probabilities[each]=(float)(degrees[each])/sum(degrees.values())
        node_probabilities_cum=[]
        prev=0
        for n,p in node_probabilities.items():
            temp=[n,prev+p]
            node_probabilities_cum.append(temp)
            prev+=p
        
        #graph should be simple;need to keep track of edges added
        #so to prevent nodes forming edges<m
        new_edges=[]
        num_edges_added=0
        target_nodes=[]
        while(num_edges_added<m):
            r=random.random()#or uniform(0,1)
            prev_cum=0
            k=0
            while(not(r>prev_cum and r<=node_probabilities_cum[k][1])):#r is not in the window
                prev_cum=node_probabilities_cum[k][1]
                k+=1
            target_node=node_probabilities_cum[k][0]
            if target_node in target_nodes:
                continue
            else:
                target_nodes.append(target_node)
            
            G.add_edge(i,target_node)
            num_edges_added+=1
            new_edges.append((i,target_node))
        print num_edges_added,' edges added'
       # display_graph(G, i, new_edges)
        
    return G
    
#this model follows power law
def plot_deg_dist(G):
    all_degrees=nx.degree(G).values()
    unique_degrees=list(set(all_degrees))
    unique_degrees.sort()
    count_of_degrees=[]
    
    for i in unique_degrees:
         c=all_degrees.count(i)
         count_of_degrees.append(c)
    print unique_degrees
    print count_of_degrees
    
    plt.plot(unique_degrees,count_of_degrees,'ro-')
    #plt.loglog(unique_degrees,count_of_degrees,'ro-')
    plt.xlabel('Degrees')
    plt.ylabel('number of nodes')
    plt.title('Degree Distribution')
    plt.show()

def main():
    n=int(raw_input('enter n'))
    m0=random.randint(2,n/5)
    G=nx.path_graph(m0)
   # display_graph(G,'','')
    G=add_nodes_barabasi(G,n,m0)
    raw_input()
    plot_deg_dist(G)
    
main()

