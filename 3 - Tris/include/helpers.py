import numpy as np
import matplotlib
import matplotlib.pyplot as plt



verbose = True
graphic = False
echange_cnt = 0
compare_cnt = 0


def echanger(T,i,j):
    global echange_cnt
    echange_cnt += 1
    T[i],T[j] = T[j],T[i]
    
def assigner(a):
    global echange_cnt
    echange_cnt += 1
    return a
 
def plus_petit(a,b):
    global compare_cnt
    compare_cnt += 1
    return a < b
    
def plus_petit_ou_egal(a,b):
    global compare_cnt
    compare_cnt += 1
    return a <= b

def afficheIteration(T,titre):
    plt.stem(T,markerfmt=',',linefmt='black',basefmt='black')
    plt.title(titre)
    plt.show()
    
def visualisation_tri_par_selection():

    T = np.random.randint(0,100,20)
    N = len(T)
    it = 0

    afficheIteration(T,'Tableau original')

    for i in range(0,N-1):
        jMin = i
        for j in range(i+1,N):
            if T[j] < T[jMin]:
                jMin = j
        T[jMin],T[i] = T[i],T[jMin]       
        it += 1
        afficheIteration(T,'Iteration {0}'.format(it))
        
def visualisation_tri_par_insertion():

    T = np.random.randint(0,100,50)
    N = len(T)
    it = 0

    afficheIteration(T,'Tableau original')

    for k in range(1,N):
        tmp = T[k]
        
        i = k
        while i > 0 and tmp < T[i-1]:
            T[i] = T[i-1]
            i -= 1
        T[i] = tmp
        
        it += 1
        if it % 7 == 0: 
            afficheIteration(T,'Iteration {0}'.format(it))

def visualisation_tri_de_shell():

    T = np.random.randint(0,100,50)
    N = len(T)
    it = 0

    afficheIteration(T,'Tableau original')

    N = len(T)
    h = 1
    while h*3 < N:
        h = 3*h+1       
    while h >= 1:      
        for j in range(1,N):
            tmp = T[j]
            i = j
            while i > h-1 and tmp < T[i-h]:
                T[i] = T[i-h]
                i -= h
            T[i] = tmp
        afficheIteration(T,'Après le {0}-tri'.format(h))
        h = h//3               
                    
def fusion_visu(T,premier,limite,dernier): 
    nb_comparaisons = nb_ecritures = 0
    
    T1 = T[premier:limite].copy()
    T2 = T[limite:dernier].copy()
    
    i = premier; i1 = i2 = 0
    
    while i1 < len(T1) and i2 < len(T2):
        nb_comparaisons += 1
        if T2[i2] < T1[i1]:
            T[i] = T2[i2]; i2 += 1; nb_ecritures += 1
        else:
            T[i] = T1[i1]; i1 += 1; nb_ecritures += 1
        i += 1

    for j in range(i1,len(T1)):
        T[i] = T1[j]; i += 1; nb_ecritures += 1

    for j in range(i2,len(T2)):
        T[i] = T2[j]; i += 1; nb_ecritures += 1
        
    return nb_comparaisons, nb_ecritures
        
def tri_fusion_recursif_visu(T,premier,dernier):      
    N = dernier - premier
    if N >= 2:          
        milieu = premier + int(N/2)
        tri_fusion_recursif_visu(T,premier,milieu)
        tri_fusion_recursif_visu(T,milieu,dernier)
        fusion_visu(T,premier,milieu,dernier)
        if N > 9:
            afficheIteration(T,"Après Fusion({0},{1},{2}) ".format(
                premier, milieu, dernier))

def visualisation_tri_fusion():
    T = np.random.randint(0,100,64)
    N = len(T)
    it = 0
    afficheIteration(T,'Tableau original')         
    tri_fusion_recursif_visu(T,0,len(T))
    
def affiche_partition(T,start,end,p):
    X = list(range(0,len(T)))
    plt.stem(X,T,markerfmt=',',linefmt='grey',basefmt='black')
    PG = [ t if i >= start and i < end and t > T[p] else 0 for i,t in enumerate(T) ]
    plt.stem(X,PG,markerfmt=',',linefmt='red',basefmt='black')
    PP = [ t if i >= start and i < end and t <= T[p] and i != p else 0 for i,t in enumerate(T) ]
    plt.stem(X,PP,markerfmt=',',linefmt='black',basefmt='black')
    PIV = [0]*len(T); PIV[p] = T[p]
    plt.stem(X,PIV,markerfmt=',',linefmt='yellow',basefmt='black')
    plt.show()
    
def affichage_debut_partition(T,premier,dernier):
    if verbose: print(T[premier:dernier-1],T[dernier-1],end=" => ")

def affichage_fin_partition(T,premier,dernier,i):
    if verbose: print(T[premier:i],T[i],T[i+1:dernier])    
    if graphic: affiche_partition(T,premier,dernier,i)
        

        
####### Test complexités       
        
def affiche_complexite(X,C1,C2,titre):
    
    X2 = [ x*x for x in X ]
    XlogX = [ x*np.log2(x) for x in X ]

    plt.title("Complexité du {}".format(titre))
    plt.loglog(X,C1,label='comparaisons')
    plt.loglog(X,C2,label='écritures ou échanges')
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
            
def evalue_complexite(algorithme, genere_tab, nom, logmax = 3):
    global compare_cnt, echange_cnt, verbose
    verbose = False
    
    C1 = []
    C2 = []
    X = [ int(x) for x in np.logspace(1,logmax,50) ]
    
    for n in X:
        compare_cnt = echange_cnt = 0
        
        T = genere_tab(n)
        algorithme(T)
        
        C1.append(compare_cnt)
        C2.append(echange_cnt)
    
    affiche_complexite(X,C1,C2,nom)
    
def tableau_aleatoire(n):
    return np.random.uniform(0,1,n)

def tableau_trie(n):
    return list(range(n))
    
def tableau_trie_inverse(n):
    return list(range(n,0,-1))
    
####### Test stabilité en toutes lettres    
    
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

####### Test stabilité visuel

def comp_int(a,b):
    return int(a) < int(b)

def comp_frac(a,b):
    return (a-int(a)) < (b - int(b))

def comp(a,b):
    return a<b

def test_stabilite(algorithme):
    T = np.random.uniform(0,7,50)
    T2 = T.copy()
    N = len(T)
    
    algorithme(T,comp_frac)
    algorithme(T,comp_int)

    algorithme(T2,comp)
    
    if (T == T2).all():
        print("\nLe tri est stable")
    else:
        print("\nLe tri n'est pas stable")
        
    plt.stem(T,markerfmt=',',linefmt='black',basefmt='black')
    plt.show()
    
def tab(N):
    return "".rjust(4-2*int(np.log2(N))) 

def affiche_entree_fusion(T,premier, limite, dernier):
    N = dernier - premier
    print(T,tab(N),"M({0},{1},{2}) ".format(premier, limite, dernier))
    
def affiche_sortie_fusion(T1,T2,T):
    print("  {0} + {1} => {2}".format(T1,T2,T))
    
def affiche_entree_tri_fusion(T,premier, dernier):
    N = dernier - premier
    print(T,tab(N),"S({0},{1})".format(premier,dernier))
