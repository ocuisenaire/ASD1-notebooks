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
    
class Graphe:
    def __init__(self,V):
        self.listes = []
        for i in range(V): self.listes.append([])
    def ajouter_arete(self,v,w):
        assert(v >= 0 and w >= 0 and 
               v < self.ordre() and 
               w < self.ordre())
        self.listes[v].append(w)
        self.listes[w].append(v)        
    def ordre(self):
        return len(self.listes)
    def taille(self):
        cnt = 0;
        for L in self.listes:
            cnt += len(L)
        return cnt // 2
    def sommets_adjacents(self,v):
        return self.listes[v]

def exemple(Type):
    G = Type(9)
    G.ajouter_arete(0,1)
    G.ajouter_arete(0,2)
    G.ajouter_arete(1,2)
    G.ajouter_arete(2,3)
    G.ajouter_arete(3,4)
    G.ajouter_arete(2,5)
    G.ajouter_arete(7,8)
    G.ajouter_arete(7,6)
    G.ajouter_arete(6,8)
    return G