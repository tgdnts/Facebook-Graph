import networkx as nx
import pyparsing
from os import system

G= nx.read_gml('listafb.gml')
G.name = "facebook"

print(nx.info(G))

print "Density ", nx.density(G)

print "Amigo mais antigo: ", G.node[0]['label']
#print ("Node    Degree Centrality      Betweenness Centrality")
#i=nx.degree_centrality(G);
#for x in range(1,G.number_of_nodes()+1):
#    print x,'            %.2f' % nx.degree_centrality(G).get(x),\
#    '                     %.2f' % nx.betweenness_centrality(G).get(x)

for x in range(1,G.number_of_nodes()):
     print "Amigos em comum com ", G.node[x]['label'], ": ", len(G.neighbors(G.node[x]['id']))
     
print "Number of connected components: ", nx.number_connected_components(G)
