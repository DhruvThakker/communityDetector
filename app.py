import networkx as nx
import infomap

"""
Generate and draw a network with NetworkX, colored
according to the community structure found by Infomap.
"""


def get_communities(edgelist):
    myInfomap = infomap.Infomap("--two-level -N 5 --silent")
    network = myInfomap.network()
    for edge in edgelist:
        network.addLink(edge[0], edge[1])
    myInfomap.run()
    communities = {}
    for node in myInfomap.iterTree():
        if node.isLeaf():
            a = node.moduleIndex()
            b = node.physicalId
            if a in communities:
                communities[a].append(b)
            else:
                communities[a] = [a]
    return communities



G = nx.karate_club_graph()

print(get_communities(list(G.edges())))