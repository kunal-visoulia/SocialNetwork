#there are no hubs in random network
import networkx as nx
import random
from __builtin__ import raw_input
from audioop import reverse

def remove_a_random_node(G):
    nodes=G.nodes()
    r=random.choice(nodes)
    G.remove_node(r)
    return G

def remove_a_high_deg_node(G):
    degrees=G.degree()
    nodes=sorted(degrees.items(),key=lambda x:x[1],reverse=True)
    #nodes is list of tuples(node,degree) in sorted manner
    G.remove_node(nodes[0][0])
    return G

def main():
    print '## For Real World Networks ##'
    G=nx.read_edgelist("F:\social nw\SocialNetwork\src\datasets\Email-Enron.txt")
    print nx.info(G)
    #print nx.is_connected(G)
    
    raw_input()
    #when does the graph becomes disconnected
    print '#### Random Removal of Nodes #####'
    G1=G.copy()
    print 'Is G1 connected? ',nx.is_connected(G1)
    nodes_removed_random=0
    
    while(nx.is_connected(G1)):
        G1=remove_a_random_node(G1)
        nodes_removed_random+=1
        print 'Is G1 connected? ',nx.is_connected(G1)
         
    print 'nodes removed when randomly chosen',nodes_removed_random 
    raw_input()
    
    print '#### Selective Removal of Nodes #####'
    G2=G.copy()
    print 'Is G2 connected? ',nx.is_connected(G2)
    nodes_removed_selective=0
    
    while(nx.is_connected(G2)):
        G1=remove_a_high_deg_node(G2)
        nodes_removed_selective+=1
        print 'Is G2 connected? ',nx.is_connected(G2)
         
    print 'nodes removed when selectively chosen to make graph disconnected',nodes_removed_selective
    ##########################################################################################################3
    print '## Random network ##'
    H=nx.erdos_renyi_graph(1000,0.2)
    print nx.info(H)
    raw_input()
    #when does the graph becomes disconnected
    print '#### Random Removal of Nodes #####'
    H1=H.copy()
    print 'Is H1 connected? ',nx.is_connected(H1)
    nodes_removed_random=0
    
    while(nx.is_connected(H1)):
        H1=remove_a_random_node(H1)
        nodes_removed_random+=1
        print 'Is H1 connected? ',nx.is_connected(H1)
         
    print 'nodes removed when randomly chosen',nodes_removed_random 
    raw_input()
    
    print '#### Selective Removal of Nodes #####'
    H2=H.copy()
   
    print nx.info(H2)
    print 'Is H2 connected? ',nx.is_connected(H2)
    nodes_removed_selective=0
    
    while(nx.is_connected(H2)):
        H2=remove_a_high_deg_node(H2)
        nodes_removed_selective+=1
        print 'Is H2 connected? ',nx.is_connected(H2)
         
    print 'nodes removed when selectively chosen to make graph disconnected',nodes_removed_selective

    
    
main()