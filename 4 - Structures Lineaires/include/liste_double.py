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

class Liste:
    def __init__(self):
        self.tete = None
        self.queue = None
        self.N = 0


class MaillonVide:
    def __init__(self):
        self.suivant = self
        self.precedent = self
        
class Liste:
    def __init__(self):
        self.__tq = MaillonVide()
        self.__N = 0
        
    __str__ = __liste_double_str__

class list_iterator:
    def __init__(self,maillon): self.__M = maillon
        
    def __str__(self): return self.__M.__str__()

    def copie(self):   return list_iterator(self.__M)
    
    def incr(self):    self.__M = self.__M.suivant
        
    def decr(self):    self.__M = self.__M.precedent
    
    def suivant(self, N = 1): 
        s = self.copie()
        for i in range(N): s.incr()
        return s
    
    def precedent(self, N = 1): 
        s = self.copie() 
        for i in range(N): s.decr()
        return s
        
    def get_val(self): return self.__M.donnee
    
    def set_val(self,val): self.__M.donnee = val
        
    def __eq__(self,other):
        return isinstance(other,list_iterator) and self.__M == other.__M

def liste_begin(L): return list_iterator(L._Liste__tq.suivant)

Liste.begin = liste_begin

def liste_end(L):  return list_iterator(L._Liste__tq)

Liste.end = liste_end

def est_vide(L):
    return L.begin() == L.end()
Liste.empty = est_vide

def taille(L):
    return L._Liste__N 
Liste.size = taille

def inserer_avant(M,val):
    N = Maillon(val,p = M.precedent, s = M)
    
def inserer_avant_en_liste(L,it,val):
    inserer_avant(it._list_iterator__M,val)
    L._Liste__N += 1
    
Liste.insert = inserer_avant_en_liste

def supprimer(M):
    assert(M and M.precedent and M.suivant)
    M.precedent.suivant = M.suivant
    M.suivant.precedent = M.precedent
    
def supprimer_en_liste(L,it):
    supprimer(it._list_iterator__M)
    L._Liste__N -= 1

Liste.erase = supprimer_en_liste

def inserer_en_tete(L,val):
    L.insert(L.begin(),val)  
    
Liste.push_front = inserer_en_tete


def supprimer_en_tete(L):
    if L.empty(): raise IndexError()
    L.erase(L.begin())
    
Liste.pop_front = supprimer_en_tete


def inserer_en_queue(L,val):
    L.insert(L.end(),val)
    
Liste.push_back = inserer_en_queue


def supprimer_en_queue(L):
    if L.empty(): raise IndexError()
    L.erase(L.end().precedent())
    
Liste.pop_back = supprimer_en_queue

def afficher_liste(L):
    it = L.begin()
    while it != L.end():
        print(it, end="")
        if it.suivant() != L.end(): 
            print(end = " ⇄ ")
        it.incr()


def supprimer_decroissances(L):
    it = L.begin(); max_val = it.get_val()
    it = it.suivant()
    
    while it != L.end():
        if it.get_val() < max_val:
            tmp = it.suivant()
            L.erase(it); 
            it = tmp
        else:
            max_val = it.get_val()
            it.incr()

def tri_par_insertion(L):
    if L.size() < 2: return
    
    k = L.begin().suivant()
    while k != L.end():
        tmp = k.get_val()
        
        j = k; i = j.precedent()
        while j != L.begin() and tmp < i.get_val():
            j.set_val(i.get_val())
            j = i.copie() 
            i.decr()
            
        j.set_val(tmp)
        k.incr()


