#changing payoff
import networkx as nx
import matplotlib.pyplot as plt

#needed to be done only once
#G=nx.erdos_renyi_graph(10,0.5)
#nx.write_gml(G,'random_graph.gml')

def set_all_B(G):
    for each in G.nodes():
        G.node[each]['action']='B'

def set_A(G,list1):
    for each in list1:
        G.node[each]['action']='A'

def get_colors(G):
    list1=[]
    for each in G.nodes():
        if G.node[each]['action']=='B':
            list1.append('red')
        else:
            list1.append('green')
    return list1

def find_neigh(node1,action,G):
    num=0
    for each in G.neighbors(node1):
        if G.node[each]['action']==action:
            num+=1
    return num

def recalculate_options(G):
    dict1={}
    # Payoff(A)=a=4
    # Payoff(A)=b=3
    a=4
    b=3
    for each in G.nodes():
        num_A=find_neigh(each,'A',G)#finds neighbour of current node that accepted action A
        num_B=find_neigh(each,'B',G)
        
        payoff_A=a*num_A
        payoff_B=b*num_B
        
        if payoff_A>=payoff_B:
            dict1[each]='A'
        else:
            dict1[each]='B'
    return dict1
    
def reset_node_attributes(G,action_dict):
    for each in action_dict:
        G.node[each]['action']=action_dict[each]

def terminate_1(c,G):
    f=1
    for each in G.nodes():
        if G.node[each]['action']!=c:
            f=0
            break
    return f

def terminate(G,count):
    flag1=terminate_1('A',G)
    flag2=terminate_1('B',G)
    if flag1==1 or flag2==1 or count>=100:
        return 1
    else:
        return 0

G=nx.read_gml('random_graph.gml')

#every node will have an attribute action and value of the action=B
set_all_B(G)

list1=[3,7]#initial adopting nodes
set_A(G,list1)

colors=get_colors(G)
nx.draw(G,node_color=colors,node_size=800,with_labels=1)
plt.show()

flag=0
count=0
while(1):
    flag=terminate(G,count)
    if flag==1:
        break
    count=count+1
    action_dict=recalculate_options(G)#dictionary with nodes as keys and their action as values
    reset_node_attributes(G,action_dict)
    colors=get_colors(G)
    nx.draw(G,node_color=colors,node_size=800,with_labels=1)
    plt.show()