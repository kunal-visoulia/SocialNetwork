import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):
    all_degrees=nx.degree(G).values()
    unique_degrees= list(set(all_degrees))
    #how many nodes have a given degree
    count_of_degrees=[]
    print('Density=',nx.density(G))
    for i in nx.clustering(G).items():
            print(i) 
    print(nx.average_clustering(G))
    print('diameter is=',nx.diameter(G))
    for i in unique_degrees:
            x=all_degrees.count(i)#tells occurences of nodes with degree i
            count_of_degrees.append(x)
    plt.loglog(unique_degrees,count_of_degrees,'ro-')
    plt.show()

# returns graph object
#G=nx.read_edgelist('datasets/facebook_combined.txt')
#G=nx.read_pajek('datasets/football.net')
#G=nx.read_graphml('datasets/vecwiki-20091230-manual-coding.graphml')
#G=nx.read_gexf('datasets/EuroSiSGeneralePays.gexf')
G=nx.read_gml('datasets/karate.gml')
print(nx.info(G))
#print(nx.number_of_edges(G))
#print(nx.number_of_nodes(G))
#print(nx.is_directed(G))
#G=nx.draw(G,with_labels=1)
#plt.show()

plot_deg_dist(G)
