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

def get_nodes_sorted_by_RW(points):
    points_array=numpy.array(points)
    #returns indices sorted by value of points
    nodes_sorted_by_RW=numpy.argsort(-points_array)#- for descending order
    return nodes_sorted_by_RW

def random_walk(G):
    nodes=G.nodes()
    RW_points=[0 for i in range(G.number_of_nodes())]
    #keeps number of times a node has been visited
    
    r=random.choice(nodes)
    RW_points[r]+=1
    out=G.out_edges(r)
    
    c=0
    while(c!=100000):
        if(len(out)==0):
            focus=random.choice(nodes)#currently visited node
        else:
            r1=random.choice(out)
            focus=r1[1]
        RW_points[focus]+=1
        out=G.out_edges(focus)
        c+=1
    return RW_points
    
def main():
    #1 create/take a directed graph with 'n'nodes
    G=nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G=add_edges(G,0.3)
    
    #2 perform random walk
    RW_points=random_walk(G)
  
    #3 get sorted nodes as per points accumulated during random walk
    nodes_sorted_by_RW=get_nodes_sorted_by_RW(RW_points)
    print nodes_sorted_by_RW
    
    #4 compare the ranks thus obtained with the ranks obtained from the inbuilt PAge Rank method
    pr=nx.pagerank(G)#returns dictionary where nodes are key and page ranks are values which is unsorted
    pr_sorted=sorted(pr.items(),key=lambda x:x[1],reverse=True)
    #pr_sorted is list of tuples
    for i in pr_sorted:
        print i[0],
    
    
main()  