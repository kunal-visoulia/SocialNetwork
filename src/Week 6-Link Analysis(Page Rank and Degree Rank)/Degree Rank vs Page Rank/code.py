import networkx as nx
import matplotlib.pyplot as plt

def main():
    G=nx.read_edgelist('F:\social nw\SocialNetwork\src\datasets\Cit-HepPh.txt',create_using=nx.DiGraph())
    deg=G.in_degree()#dictionary
    pr=nx.pagerank(G)#dictionary
    
    pr_values=[]
    #contains the page rank values of nodes in the same order they appear in deg dictionary
    
    for i in deg.keys():
        pr_values.append(pr[i])
        
    plt.plot(deg.values(),pr_values,'ro',markersize=3)
    plt.xlabel('Degrees of the nodes')
    plt.ylabel('Page Rank Values of nodes')
    plt.show()
    
main()

#result: the graph is non linear,thus, pagerank and degreerank are not correlated
#in terms of citation n/w this means that there are pages that are citated by many nodes(large indegree)
#but have low page rank(they are not that important) and vice versa