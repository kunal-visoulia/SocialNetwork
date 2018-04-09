import networkx as nx


edge_list = [(0, 3), (0, 5), (1, 2), (1, 4), (1, 5), (2, 4), (2, 6), (3, 5), (3, 6), (4, 5),
             (5, 6), (5, 2), (5, 8), (6, 3), (7, 4), (7, 8), (7, 0), (8, 9), (9, 0), (9, 3)]
G = nx.DiGraph(edge_list)
#"Enter the node to get its in-degree centrality rank: "
n = int(raw_input())
if nx.is_strongly_connected(G):
    s_c =1
else:
    s_c = 0

if nx.is_weakly_connected(G):
    w_c =1
else:
    w_c = 0

in_degree_centrality = nx.in_degree_centrality(G)


    
sorted_IDC = sorted(in_degree_centrality.items(), key=lambda t: t[1], reverse=True)

node_list = [point[0] for point in sorted_IDC]

in_degree_list=in_degree_centrality.values()

ranks = {x:node_list.index(x)+1 for x in node_list}

rank=ranks.values()
temp=ranks.values()
print in_degree_list
print rank
l=list(set(in_degree_centrality.values()))
print l
for value in l:
    cnt = in_degree_centrality.values().count(value)
    indices = [i for i, x in enumerate(in_degree_centrality.values()) if x == value] 
    print indices
      
    if(cnt>0):
        for each in indices:
            val=0
            for each2 in indices:
                val+= temp[each2]
                print val
            rank[each]=((float)(val)/(float)(cnt))
            
print rank
rank_node_n = rank[n]
result =(s_c, w_c, rank_node_n)

print(result)