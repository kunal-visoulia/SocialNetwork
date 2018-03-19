# Type your code here
#prefix
import networkx as nx

G = nx.Graph()
G.add_edges_from([[0, 2], [0, 4], [0, 7], [1, 3], [1, 7], [1, 9], [2, 3], [2, 5],
                  [3, 5], [3, 9], [4, 9], [4, 6], [5, 6], [5, 8], [6, 7], [8, 9]])

action_A = [1, 3, 5, 7]
action_B = [2, 4, 6, 8]
action_C = [0, 9]
#"Enter the pay off for the actions A, B and C seperated by the space: "
pa, pb, pc = map(int, raw_input().split())
def find_neigh(node1,action,G):
    num=0
    for each in G.neighbors(node1):
        if G.node[each]['action']==action:
            num+=1
    return num

def recalculate_options(G,pa,pb,pc):
    dict1={}
    for each in G.nodes():
        num_A=find_neigh(each,'A',G)
        num_B=find_neigh(each,'B',G)
        num_C=find_neigh(each,'C',G)
        
        payoff_A=pa*num_A
        payoff_B=pb*num_B
        payoff_C=pc*num_C
        
        if payoff_A>=payoff_B  and payoff_A>=payoff_C:
            dict1[each]='A'
        
        elif payoff_B>=payoff_A  and payoff_B>=payoff_C:
            dict1[each]='B'
        
        elif payoff_C>=payoff_A  and payoff_C>=payoff_B:
            dict1[each]='C'
    return dict1
    
def reset_node_attributes(G,action_dict):
    for each in action_dict:
        G.node[each]['action']=action_dict[each]
        
def set_action(G):
    for each in action_A:
        G.node[each]['action']='A'
    
    for each1 in action_B:
        G.node[each1]['action']='B'
    
    for each2 in action_C:
        G.node[each2]['action']='C'
    
set_action(G)
action_dict=recalculate_options(G,pa,pb,pc)
for each in G.node.values():
    print(each)
reset_node_attributes(G,action_dict)
a=0
b=0
c=0
print("\n") 
for each in G.node.values():
    print(each)
    if each['action']=='A':
        a+=1
    
    elif each['action']=='B':
        b+=1
    
    elif each['action']=='C':
        c+=1
    
print([a,b,c])