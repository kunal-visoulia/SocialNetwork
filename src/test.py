import networkx as nx
import matplotlib.pyplot as plt
cities = ["Tuticorin", "Chennai", "Mumbai", "New Delhi", "Chandigarh"]
air_travel_time = {("Tuticorin", "Chennai"):80,
                 ("Chennai", "Mumbai"):110, 
                 ("Chennai", "New Delhi"):170, 
                 ("Mumbai", "New Delhi"):130,
                 ("New Delhi", "Chandigarh"):55}
G=nx.Graph()

for each_city in cities:
        G.add_node(each_city)         
for i in air_travel_time.items():
    G.add_edge(i[0][0],i[0][1],weight=i[1])

'''pos=nx.circular_layout(G)

nx.draw(G,pos,with_labels=1)
nx.draw_networkx_edge_labels(G,pos)
plt.show()'''
list1=[]
list2=[]
def shortest_air_route(city1,city2):
    G=nx.Graph()
    for each_city in cities:
        G.add_node(each_city)         
    for i in air_travel_time.items():
        G.add_edge(i[0][0],i[0][1],weight=i[1])
    if(city1==city2):
        return ([],0)
    list1=nx.dijkstra_path(G,city1,city2)
    dist=nx.dijkstra_path_length(G, city1, city2)
    return(list1,dist)
    
x=shortest_air_route('Mumbai','Chandigarh')
print(x)
    