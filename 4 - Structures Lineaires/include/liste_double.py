class Maillon:
    def __init__(self, v, s = None, p = None):
        self.donnee = v
        self.suivant = s 
        self.precedent = p 

        if s: s.precedent = self 
        if p: p.suivant = self
            
    def __str__(self): 
        return "{}".format(self.donnee)

def __liste_double_str__(L):
    if L.empty(): return "⌀"
    m = L._Liste__tq.suivant
    s = "⌀ ← "
    while m != L._Liste__tq:
        s += m.__str__()
        s += " ⇄ " if m.suivant != L._Liste__tq else " → ⌀"
        m = m.suivant
    return s

class MaillonVide:
    def __init__(self):
        self.suivant = self
        self.precedent = self
        
class Liste:
    def __init__(self):
        self.__tq = MaillonVide()
        self.__N = 0
        
    __str__ = __liste_double_str__


def debut(L):     return L._Liste__tq.suivant

def fin(L):       return L._Liste__tq

def suivant(m):   return m.suivant

def precedent(m): return m.precedent

def get_val(m):   return m.donnee

def set_val(m,v): m.donnee = v


def est_vide(L):
    return debut(L) == fin(L)
Liste.empty = est_vide

def taille(L):
    return L._Liste__N 
Liste.size = taille

def inserer_avant(M,val):
    N = Maillon(val,p = M.precedent, s = M)
    
def inserer_avant_en_liste(L,M,val):
    inserer_avant(M,val)
    L._Liste__N += 1
    
Liste.insert = inserer_avant_en_liste

def supprimer(M):
    assert(M and M.precedent and M.suivant)
    M.precedent.suivant = M.suivant
    M.suivant.precedent = M.precedent
    
def supprimer_en_liste(L,M):
    supprimer(M)
    L._Liste__N -= 1

Liste.erase = supprimer_en_liste


def inserer_en_tete(L,val):
    L.insert(debut(L),val)  
    
Liste.appendleft = inserer_en_tete


def supprimer_en_tete(L):
    if L.empty(): raise IndexError()
    L.erase(debut(L))
    
Liste.popleft = supprimer_en_tete


def inserer_en_queue(L,val):
    L.insert(fin(L),val)
    
Liste.append = inserer_en_queue

def supprimer_en_queue(L):
    if L.empty(): raise IndexError()
    L.erase(precedent(fin(L)))
Liste.pop = supprimer_en_queue


def r_debut(L):     return L._Liste__tq.precedent

def r_fin(L):       return L._Liste__tq

def r_suivant(m):   return m.precedent

def r_precedent(m): return m.suivant
