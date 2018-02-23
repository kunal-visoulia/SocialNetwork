# Prefix
import networkx as nx
cities = ["Tuticorin", "Chennai", "Mumbai", "New Delhi", "Chandigarh"]
air_travel_time = {("Tuticorin", "Chennai"):80,
                 ("Chennai", "Mumbai"):110, 
                 ("Chennai", "New Delhi"):170, 
                 ("Mumbai", "New Delhi"):130,
                 ("New Delhi", "Chandigarh"):55}
#"Enter the indices of city 1 and city 2 sepearted by space: "
city_indices = map(int, raw_input().split())
try:
    city1 = cities[city_indices[0]]
    city2 = cities[city_indices[1]]
except IndexError as e:
    print (e)

list1=[]
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
           
           


assert shortest_air_route("Mumbai", "Chandigarh") == (['Mumbai', 'New Delhi', 'Chandigarh'], 185)
assert shortest_air_route("Chennai", "Chandigarh")[1] == shortest_air_route("Chandigarh", "Chennai")[1]
print shortest_air_route(city1, city2)
