#just a comment
import networkx as nx
import matplotlib.pyplot as plt
import random as rn
import math
def create_graph():
    G=nx.Graph()

    #two ways
    #G.add_nodes_from(range(1,101))
    for i in range(1,101):
        G.add_node(i)
    return G

def visualize(G,labeldict,nsize,clr):
    nx.draw(G,labels=labeldict,with_labels=1,node_size=nsize,node_color=clr)
    plt.show()

def assign_bmi(G):
    #ranges from 15-40
    for each in G.nodes():
        G.node[each]['name']=rn.randint(15,40)
        G.node[each]['type']='person'

def get_labels(G):
    dict1={}
    for each in G.nodes():
        dict1[each]=G.node[each]['name']
    #key is node and value is bmi of that node
    return dict1

def get_size(G):
    array1=[]
    for each in G.nodes():
        if G.node[each]['type']=='person' :
            array1.append(G.node[each]['name']*20)
        else:
            array1.append(1000)
    return array1

def add_foci_nodes(G):
    n=G.number_of_nodes()+1
    foci_nodes=['gym','eatout','movi club','karate club','yoga club']
    for j in range(0,5):
        G.add_node(n)
        G.node[n]['name']=foci_nodes[j]
        G.node[n]['type']='foci'
        n=n+1

def get_colors(G):
    c=[]
    for each in G.nodes():
        if G.node[each]['type']=='person':
            if G.node[each]['name']==15:
                c.append('green')
            elif G.node[each]['name']==40:
                c.append('yellow')
            else:
                c.append('blue')
        else:
            c.append('red')
    return c

def get_foci_nodes():
    f=[]
    for each in G.nodes():
        if G.node[each]['type']=='foci':
            f.append(each)
    return f

def get_persons_nodes():
    p=[]
    for each in G.nodes():
        if G.node[each]['type']=='person':
            p.append(each)
    return p

def homophily(G):
    #add edge if two people have similar bmi
    person_nodes=get_persons_nodes()
    for u in person_nodes:
        for v in person_nodes:
            if u!=v:
                diff=abs(G.node[u]['name']-G.node[v]['name'])
                p=float(1)/(diff+5000)
                r=rn.uniform(0,1)
                if r<p:
                    G.add_edge(u,v)
            

def add_foci_edges(G):
    foci_nodes=get_foci_nodes()
    person_nodes=get_persons_nodes()
    for each in person_nodes:
        r=rn.choice(foci_nodes)
        G.add_edge(each,r)

def commonneigh(u,v,G):
    nu=set(G.neighbors(u))
    nv=set(G.neighbors(v))
    return len(nu & nv)
    

def closure(G):
    array1=[]#addition every edge should be independent of another node1,node2,probability
    for u in G.nodes():
        for v  in G.nodes():
            if u!=v and (G.node[u]['type']=='person' or G.node[v]['type']=='person'):
                k=commonneigh(u,v,G)
                p=1-math.pow(1-0.1,k)#every common friend gives prob 0.1
                tmp=[]
                tmp.append(u)
                tmp.append(v)
                tmp.append(p)
                array1.append(tmp)
    for each in array1:
        u=each[0]
        v=each[1]
        p=each[2]
        r=rn.uniform(0,1)
        if(r<p):
            G.add_edge(u,v)
                       
G=create_graph()
assign_bmi(G)
add_foci_nodes(G)
labeldict=get_labels(G)
nodesize=get_size(G)
color_array=get_colors(G)
add_foci_edges(G)
homophily(G)# commented: no homophily as of now, common neighbors will exist only if they are part of same foci 
#puts edge between two peoples
visualize(G,labeldict,nodesize,color_array)
while 1:# to observe membership closure
    closure(G) #foci closure
    #puts edge between two people if they have same foci
    visualize(G,labeldict,nodesize,color_array)

