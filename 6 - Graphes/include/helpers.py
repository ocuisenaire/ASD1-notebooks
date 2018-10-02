from graphviz import Graph

def afficher_graphe(g):
    
    G = Graph(engine = 'neato')
    for v in range(g.ordre()):
        G.node('{}'.format(v))
    for v in range(g.ordre()):
        for w in g.sommets_adjacents(v):
            if v < w:
                G.edge('{}'.format(v),'{}'.format(w))
    display(G)