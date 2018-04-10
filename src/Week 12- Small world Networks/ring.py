import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy
def add_edges(G):
    list_nodes=G.nodes()
    n=G.number_of_nodes()
    #every nodes in this list is supposed to be connected to 2 nodes on right and left each
    for i in range(0,len(list_nodes)):
        #print list_nodes[i], list_nodes[i+1], list_nodes[i-1], list_nodes[i+2], list_nodes[i-2]
        #-ve indices pose no problem, but
        #when i+1 or i+2->n, we need to set this value to 0
        #                ->n+1, we need to set this to 1 
        G.add_edge(list_nodes[i],list_nodes[i-1])
        G.add_edge(list_nodes[i],list_nodes[i-2])
        target=i+1
        if target>n-1:
            target=target-n
            G.add_edge(list_nodes[i],target)
        else:
            G.add_edge(list_nodes[i],target)
        target=i+2
        if target>n-1:
            target=target-n
            G.add_edge(list_nodes[i],target)
        else:
            G.add_edge(list_nodes[i],target)

def add_long_link(G):
    v1=random.choice(G.nodes())
    v2=random.choice(G.nodes())
    while(v1==v2):
        v1=random.choice(G.nodes())
        v2=random.choice(G.nodes())
    G.add_edge(v1,v2)
def find_best_neighbor(G,c,v):
    dis=G.number_of_nodes()
    for each in G.neighbors(c):
        dis1=len(nx.shortest_path(H, source=each,target=v))
        if dis1<dis:
            dis=dis1
            choice=each
    return choice
    
def myopic_search(G,u,v):     
    path=[u]
    current=u
    while(1):
        w=find_best_neighbor(G,current,v)
        path.append(w)
        current=w
        if current==v:
            break
    return path 

def set_path_colors(G,p,p1):
    c=[]
    for each in G.nodes():
        if each==p1[0]:
            c.append('orange')
        if each==p1[len(p1)-1]:
            c.append('orange')
        if each in p and p1 and each!=p1[0] and each!=p1[len(p1)-1]:
             c.append('yellow')
        if each in p and each not in p1:
             c.append('blue')
        if each in p1 and each not in p:
             c.append('green')    
        if each not in p1 and each not in p:
            c.append('white')
    return c

x1=[] #number of nodes
y1=[] #time taken for myopic search
for num in [100,200,300,400,500,600,700,800,900,1000]:    
    G=nx.Graph()
    G.add_nodes_from(range(0,num))

    add_edges(G)  #add ties based on homophily

    '''#prints ties
    for each in G.nodes():
    print each,':',
    for each1 in G.neighbors(each):
        print each1,
    print '\n'
    '''
    '''we do this before adding long ties because for myopic search we look at source's all neighbors, and from these neighbors we calculate distance from target node.
    We re not aware of week ties a neighbor node makes, so we take the graph with only homophily based ties.
    We do search in G but calculate distance in H'''
    H=G.copy()
    m=[] #path lengths corrsponding to the myopic search
    #o=[] #path lengths corrsponding to the optimal search
    #x=[] #each point on x axis is one pair of diametrically opposite node- (0,50),(1,51)
    l=0 
    while(l<=G.number_of_nodes()/10): #number of weak ties= 105 of number of nodes
        add_long_link(G)
        l+=1
    t=0
    for u in range(0,(G.number_of_nodes()/2)-1):
        v=u+G.number_of_nodes()/2
        p=myopic_search(G,u,v)
        #p1=nx.shortest_path(G,source=u,target=v)
        m.append(len(p))
        #o.append(len(p1))
        #x.append(t)
        t+=1
    print G.number_of_nodes(), numpy.average(m)
    y1.append(numpy.average(m))
    x1.append(G.number_of_nodes())
    #print m
    #print x
    #print o 
    #nx.draw(G,with_labels=1)
    #plt.show()

plt.plot(x1,y1)
        #plt.plot(x,m,'r')
        #plt.plot(x,o,'b')
plt.show()

'''
x=[0]
y=[nx.diameter(G)] 
t=0 
while(t<=100):
    add_long_link(G)
    t+=1
    x.append(t)
    y.append(nx.diameter(G))
plt.xlabel('Number of weak ties added')
plt.ylabel('Diameter')
plt.plot(x,y)
plt.show()'''
'''
p=myopic_search(G, 0,40)
p1=nx.shortest_path(G, source=0, target=40)
print p1
print p

colors=set_path_colors(G,p,p1)
print colors
nx.draw(G,with_labels=1,node_color=colors)
plt.show()
'''

