import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy


def independentcascade(G,s):
    just_infected=list(s)
    infected=list(s)
    while(1):
        if len(just_infected)==0:
            return infected
        tmp=[]
        for each in just_infected:
            for each1 in G.neighbors(each):
                r=random.uniform(0,1)
                if r<0.5 and each1 not in infected and each1 not in tmp:
                    tmp.append(each1)
        for each in tmp:
            infected.append(each)
        just_infected=list(tmp)
                
    
G=nx.Graph()
G.add_edges_from([(1,2),(3,11),(4,5),(5,6),(5,7),(5,8),(5,9),(5,10),(10,11),(10,13),(11,13),(12,14),(12,15),(13,14),(13,15),(13,16),(13,17),(14,15),(14,16),(15,16)])

dict_degree={}
dict_closeness={}
dict_beweeness={}
dict_coreness={}
  
for each in G.nodes():
    dict_degree[each]=G.degree(each)
    dict_closeness[each]=nx.closeness_centrality(G,each)
    dict_beweeness[each]=nx.betweenness_centrality(G,each)
    dict_coreness[each]=nx.core_number(G)[each]

dict_cascade={} #holds cascading power of nodes

for each in G.nodes():
    c=[]
    for num in range(0,1000): #cascade is random thus we average out total number of infected people for 1000 iteration
        seed=[each]
        i=independentcascade(G,seed)
        c.append(len(i))
    dict_cascade[each]=numpy.average(c)
sorted_dict_cascade=sorted(dict_cascade,key=dict_cascade.get,reverse=True)
sorted_dict_deg=sorted(dict_degree,key=dict_degree.get,reverse=True)
sorted_dict_co=sorted(dict_coreness,key=dict_coreness.get,reverse=True)
sorted_dict_cl=sorted(dict_closeness,key=dict_closeness.get,reverse=True)
sorted_dict_bw=sorted(dict_beweeness,key=dict_beweeness.get,reverse=True)

print  'nodes sorted accd. to degree'
print sorted_dict_deg
print  'nodes sorted accd. to closeness'
print sorted_dict_cl
print  'nodes sorted accd. to betweeness'
print sorted_dict_bw
print  'nodes sorted accd. to coreness'
print sorted_dict_co
print  'nodes sorted accd. to influence'
print sorted_dict_cascade
         