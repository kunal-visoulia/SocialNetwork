import networkx as nx 
import random
import numpy

def add_edges(G,p):
    #analogy:the coin is biases towards heads with a prob p
    #way to create random graphs
    for i in G.nodes():
        for j in G.nodes():
            if i!=j:
                r=random.random()
                if r<=p:#means we got a head
                   G.add_edge(i,j)#directed edges
                else:
                    continue 
    return G

def initialize_points(G):
    points=[100 for i in range(G.number_of_nodes())] 
    return points

def distribute_points(G,points):
    prev_points=points
    new_points=[0 for i in range(G.number_of_nodes())]
    
    for i in G.nodes():
        out=G.out_edges(i)
        if len(out)==0:
            new_points[i]+=prev_points[i]#cuz even though there are no outlinks the might be some inlnks
        else:
            share=(float)(prev_points[i])/len(out)
            for each in out:
                new_points[each[1]]+=share
    return G,new_points       

def handle_points_sink(G,points):
    for i in range(len(points)):
        points[i]=(float)(points[i])*0.8 
    
    #total number of points in graph never change
    n=G.number_of_nodes()
    extra=(float)(n*100*0.2)/n
    for i in range(len(points)):
        points[i]+=extra
    return points
    
def keep_distributing_points(G,points):
    prev_points=points
    print 'Enter 3 to stop'
    while(1):
        G,new_points=distribute_points(G, prev_points)
        print new_points
        
        #point sink occurs when there are nodes with no outlink and it starts accumulating all the points
        #handling point sink by taking 20% points from every node and distributing it equally to all nodes
        new_points=handle_points_sink(G,new_points)
        
        char=raw_input()
        if char=='3':
            break
        prev_points=new_points
    return G,new_points
    

def get_nodes_sorted_by_points(points):
    points_array=numpy.array(points)
    #returns indices sorted by value of points
    nodes_sorted_by_points=numpy.argsort(-points_array)#- for descending order
    return nodes_sorted_by_points
    
           
def main():
    #create/take a directed graph with 'n'nodes(nx.gnrgraph gives directed graph)
    G=nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G=add_edges(G,0.3)
    
    #assign 100 points to each node
    points=initialize_points(G)
    print points
    
    #keep distributing points until convergence
    G,points=keep_distributing_points(G,points)
    
    #get node's ranking as per the points accumulated
    nodes_sorted_by_points=get_nodes_sorted_by_points(points)
    print nodes_sorted_by_points
    
    #compare the ranks thus obtained with the ranks obtained from the inbuilt PAge Rank method
    pr=nx.pagerank(G)#returns dictionary where nodes are key and page ranks are values which is unsorted
    pr_sorted=sorted(pr.items(),key=lambda x:x[1],reverse=True)
    #pr_sorted is list of tuples
    for i in pr_sorted:
        print i[0],
    
    
main()  