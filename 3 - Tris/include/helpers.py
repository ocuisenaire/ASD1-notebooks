import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def afficheIteration(T,it):
    plt.stem(T,markerfmt=',',linefmt='black',basefmt='black')
    plt.title('Iteration {0}'.format(it))
    plt.show()
    
def visualisation_tri_par_selection():

    T = np.random.randint(0,100,20)
    N = len(T)
    it = 0

    afficheIteration(T,it)

    for i in range(0,N-1):
        jMin = i
        for j in range(i+1,N):
            if T[j] < T[jMin]:
                jMin = j
        T[jMin],T[i] = T[i],T[jMin]       
        it += 1
        afficheIteration(T,it)
        
def affiche_complexite(X,C1,C2,titre):
    
    X2 = [ x*x for x in X ]
    XlogX = [ x*np.log2(x) for x in X ]

    plt.title("Complexité du {}".format(titre))
    plt.loglog(X,C1,label='comparaisons')
    plt.loglog(X,C2,label='echanges')
    plt.loglog(X,X2,label='quadratique',linestyle='dotted')
    plt.loglog(X,XlogX,label='linéarithmique',linestyle='dotted')
    plt.loglog(X,X,label='linéaire',linestyle='dotted')
    plt.legend()
    plt.show() 
        
    print("{:>5} |{:>10} |{:>10}".format("N","Comp.","Ech."))
    print("-------------------------------")
    for i,(x,c1,c2) in enumerate(zip(X,C1,C2)):
        if i % int(len(X)/7) == 0:
            print("{:>5} |{:>10} |{:>10}".format(x,c1,c2))
            
def evalue_complexite(algorithme, genere_tab, nom):
    
    C1 = []
    C2 = []
    X = [ int(x) for x in np.logspace(1,3,50) ]
    
    for n in X:
        T = genere_tab(n)
        comp, ech = algorithme(T)
        C1.append(comp)
        C2.append(ech)
    
    affiche_complexite(X,C1,C2,nom)
    
def tableau_aleatoire(n):
    return np.random.uniform(0,1,n)

def tableau_trie(n):
    return list(range(n))
    
def tableau_trie_inverse(n):
    return list(range(n,0,-1))
    
def tableau_de_noms():
    TAB = []
    TAB.append( ("Aubert","Beatrice") )
    TAB.append( ("Caron","Alain") )
    TAB.append( ("Bonnet","Christine") )
    TAB.append( ("Bonnet","Anne") )
    TAB.append( ("Aubert","Alexandre") )
    TAB.append( ("Caron","Catherine") )
    TAB.append( ("Bonnet","Benoit") )
    TAB.append( ("Aubert","Denis") )
    TAB.append( ("Aubert","Carole") )
    TAB.append( ("Caron","Brigitte") )
    return TAB

def afficher_noms(T):
    print("{:>10}".format("Nom"),"|","{:>10}".format("Prénom"))
    print("-----------+-----------")
    for nom,prenom in T:
         print("{:>10}".format(nom),"|","{:>10}".format(prenom))

def compare_prenoms(a,b):
    return a[1] < b[1]

def compare_noms(a,b):
    return a[0] < b[0]



