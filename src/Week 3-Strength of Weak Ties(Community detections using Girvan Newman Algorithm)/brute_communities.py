import networkx as nx
import itertools as it
def comm_brute(G):
     nodes=G.nodes()
     n=G.number_of_nodes()
     first_comm=[]
     for i in range(1,n/2+1):
        comb=[list(x) for x in it.combinations(nodes,i)]
        first_comm.extend(comb)
        
    
        
     second_comm=[]
     l=[]
     for i in range(len(first_comm)):
             l=list(set(nodes)-set(first_comm[i]))
             second_comm.append(l)
     print first_comm
     print second_comm
    
        
     #which division is the best
     num_intra_edges1=[]#for first comm
     num_intra_edges2=[]#for second comm
     num_inter_edges=[]
     ratio=[]#no. of intra/no. of inter comm edges
    
     for i in range(len(first_comm)):
         num_intra_edges1.append((G.subgraph(first_comm[i])).number_of_edges())
         
     for i in range(len(second_comm)):
         num_intra_edges2.append((G.subgraph(second_comm[i])).number_of_edges())
    
     e=G.number_of_edges()
    
     for i in range(len(first_comm)):
         num_inter_edges.append(e-num_intra_edges1[i]-num_intra_edges2[i])
     for i in range(len(first_comm)):
         ratio.append((float)((num_intra_edges1[i]+num_intra_edges2[i])/num_inter_edges[i]))
     max_value=max(ratio)
     max_index=ratio.index(max_value)
     print(first_comm[max_index],second_comm[max_index])

G=nx.barbell_graph(6,0)
comm_brute(G)
          

'''for i in range(1,3):
        comb=[list(x) for x in it.combinations([1,2,3,4],i)]
        first_comm.extend(comb) 
>>> print(first_comm)
[[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]'''

'''a community has lots of intracommunity edges and very less intercomm edges So if the division
is good than no. of intracomm edges>intercookmm edges'''
        
