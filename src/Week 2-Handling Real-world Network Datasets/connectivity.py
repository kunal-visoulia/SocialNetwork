import networkx as nx
import random as rn
import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#add n modes in graph
def add_nodes(n):
    G=nx.Graph()
    G.add_nodes_from(range(n))
    return G

#add a random edge
def add_random_edge(G):
    v1=rn.choice(G.nodes())
    v2=rn.choice(G.nodes())
    if(v1!=v2):
        G.add_edge(v1,v2)
    return G

#keeps adding random edges till graph becomes connected
def add_till_connectivity(G):
    while(nx.is_connected(G)==False):
        G=add_random_edge(G)
    return G
       
def create_instances(n):
    G=add_nodes(n)
    G=add_till_connectivity(G)
    return G.number_of_edges()

#average it over 10 instances
def average_instance(n):
    list1=[]
    for i in range(0,10):
        list1.append(create_instances(n))
    return numpy.average(list1)

#plot for number of edges required for connectedness for different number of nodes
def plot_connect():
    x=[]
    y=[]
    i=10 #i= number of nodes
    while(i<200):
        print(i)
        x.append(i)
        y.append(average_instance(i))
        i=i+10
    plt.xlabel('number of nodes')
    plt.ylabel('number of edges required to connect the graph')
    plt.title('emergence of connectivity')
    plt.plot(x,y,'r')
    
    x1=[]
    y1=[]
    i=10 #i= number of nodes
    while(i<200):
        x1.append(i)
        y1.append(i*float(numpy.log(i))/2)#number of nodes required to make a graph connected is of order nlogn
        i=i+10
    plt.plot(x1,y1,'y')
    plt.show()
plot_connect()