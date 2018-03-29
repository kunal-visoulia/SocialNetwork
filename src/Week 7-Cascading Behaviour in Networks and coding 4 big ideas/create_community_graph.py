#for idea 3
import networkx as nx
import random
import matplotlib.pyplot as plt

G=nx.Graph()

def create_first_comm(G):
    for i in range(0,10):
        G.add_node(i)
        for j in range(0,10):
            if i<j:
                r=random.uniform(0,1)
                if r<0.5:
                    G.add_edge(i,j)
                    
def create_sec_comm(G):    
     for i in range(11,20):
        G.add_node(i)
        for j in range(11,20):
            if i<j:
                r=random.uniform(0,1)
                if r<0.5:
                    G.add_edge(i,j)
                    
create_first_comm(G)
create_sec_comm(G)
G.add_edge(5,15)

#nx.draw(G,with_labels=1)
#plt.show()

nx.write_gml(G,'Random_graph_community.gml')


