import networkx as nx
import pyparsing
from operator import itemgetter
from os import system

#G = nx.read_gml('logica.gml')
#G.name = "Amigos de Ana Logica"
G = nx.read_gml('listafb.gml')
G.name = "Amigos de Tiago"

no_nome = nx.get_node_attributes(G, "label")
nome_no = dict((name,node) for node,name in no_nome.items())

print(nx.info(G))

print "Density: ", nx.density(G), '\n'

print "Amigo mais antigo: ", G.node[0]['label'], '\n'

degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

degree_centrality = sorted(degree_centrality.items(), key=itemgetter(1), reverse=True)
betweenness_centrality = sorted(betweenness_centrality.items(), key=itemgetter(1), reverse=True)

print ("Node            Nome            Degree Centrality")
for x in range(0,5):
    print x,'            ', no_nome[degree_centrality[x][0]],\
    '                    %.2f' % degree_centrality[x][1]

print ''

print ("Node            Nome            Betweenness Centrality")
for x in range(0,5):
    print x,'            ', no_nome[betweenness_centrality[x][0]],\
    '                    %.2f' % betweenness_centrality[x][1]

#for x in range(0,G.number_of_nodes()):
#     print "Amigos em comum com ", G.node[x]['label'], ": ", len(G.neighbors(G.node[x]['id']))

print ''

print "Number of connected components: ", nx.number_connected_components(G)

print ''

larissa = nome_no["Larissa Leite"]
amigos_larissa = G.neighbors(larissa)

sugestoes = 0

for i in range(0, len(degree_centrality)):

	if degree_centrality[i][0] != larissa and degree_centrality[i][0] not in amigos_larissa:
		sugestoes += 1
		print "Sugestao para Larissa Leite: ", no_nome[degree_centrality[i][0]]
		
		if sugestoes >= 3:
			break
