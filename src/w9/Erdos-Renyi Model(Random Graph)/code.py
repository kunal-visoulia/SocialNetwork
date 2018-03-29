'''
In this model, each edge has a probability of being present or absent, regardless of other edges
We start with a network of n nodes and no edges. We take each pair of edge, and add an edge with probability p.
'''
#steps for implementation
'''
Take n(total number of nodes) from the user
Take p(probability by which to add edge) from the user
Create an empty graph. add n nodes to it.
Add edges to the graph randomly:-
   Take a pair of nodes.
   Get a random number r.
   If r<p, add this edge, else ignore.
   Repeat for all possible pair of nodes
'''
import networkx as nx
import matplotlib.pyplot as plt
import random
def display_graph(G,i,ne):
    #i=new node to be added,ne is the list of new edges added
    pos=nx.circular_layout(G)
    if i=='' and ne=='':
        new_node=[]
        rest_nodes=G.nodes()
        new_edges=[]
        rest_edges=G.edges()
    elif i=='':
        #new_node=[i]
        #rest_nodes=list(set(G.nodes())-set(new_node))
        rest_nodes=G.nodes()
        new_edges=ne
        rest_edges=list(set(G.edges())-set(new_edges)-set([(b,a) for (a,b) in new_edges]))
    #nx.draw_networkx_nodes(G, pos, nodelist=new_node, node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=rest_nodes, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=new_edges, edge_color='g',style='-.')
    nx.draw_networkx_edges(G, pos, edgelist=rest_edges, edge_color='r')
    plt.show()

def erdos_renyi(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r=random.random()
                if r<=p:
                    G.add_edge(i,j)
                    ne=[(i,j)]
                    #display_graph(G, '', ne)
                else:
                    ne=[]
                   # display_graph(G,'' , ne)
                    continue

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
    n= int(raw_input("enter n"))
    p= float(raw_input("enter p"))
    G=nx.Graph()
    G.add_nodes_from([x for x in range(n)])
    display_graph(G,'','')
    erdos_renyi(G,p)
    plot_deg_dist(G)
    
main()    