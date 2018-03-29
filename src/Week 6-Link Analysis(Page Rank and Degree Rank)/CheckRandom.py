'''
Created on Feb 26, 2018

@author: KUNAL
'''
#is it possible to completely traverse a graph when you choose from which node to go from current node, randomly
#(analogy:complete traversal of web graph,is it possible)
import random
import networkx as nx
import matplotlib.pyplot as plt
import numpy #for average()

#walk generates a random graph with n nodes 
#and p be the probability of edge creation 
def walk(n,p):
    start=random.randint(0,n-1)
    G=nx.erdos_renyi_graph(n, p)
    S=set([])
    v=start
    count=0
    #keep walking from a randomly selected starting node 
    #from set of the graph till all the nodes are traversed
    while(len(S)<n):
        Nbr=nx.neighbors(G, v)
        v=random.choice(Nbr)
        S.add(v)# as S is a set so adding an already present node would not change the cardinality of set
        count=count+1
        #count is the number of times the loop runs to traverse all nodes
    return count

l=[]
for i in  range (20,300):
    z=[]
    for j in range(10):
        z.append(walk(i,0.3))
        #running walk for different number of nodes 10 times
        #add taking the average of those 10 iterations for count
    l.append(numpy.average(z))
    print(i,"--->",numpy.average(z))
    
plt.plot(l)
plt.xlabel("no of nodes in graph")
plt.ylabel("no of attempts it takes to full traverse the graph")
plt.show()
