import numpy as np
import matplotlib.pyplot as plt

def affiche_complexite_1(Tableau,fn):
    C = []
    X = [ int(x) for x in np.logspace(1,4,400) ]
    
    for n in X:
        cnt = 0
        T = Tableau()
        for i in range(n):
            cnt += fn(T,i)
        C.append(cnt)

    X2 = [ x*x for x in X ]
    XlogX = [ x*np.log2(x) for x in X ]

    plt.title("Complexité")
    plt.loglog(X,C,label='écritures')
    plt.loglog(X,X,label='linéaire',linestyle='dotted')
    plt.loglog(X,XlogX,label='linéarithmique',linestyle='dotted')
    plt.loglog(X,X2,label='quadratique',linestyle='dotted')
    plt.legend()
            
    plt.show() 
    
def affiche_complexite_2(Tableau,fn):
    C = []
    X = [ int(x) for x in np.linspace(1,600,600) ]
    
    for n in X:
        cnt = 0
        T = Tableau()
        for i in range(n):
            cnt += fn(T,i)
        C.append(cnt)

    X2 = [ x*2 for x in X ]
    X3 = [ x*3 for x in X ]
    X4 = [ x*4 for x in X ]

    plt.title("Complexité")
    plt.plot(X,C,label='écritures')
    plt.plot(X,X,label='1x',linestyle='dotted')
    plt.plot(X,X2,label='2x',linestyle='dotted')
    plt.plot(X,X3,label='3x',linestyle='dotted')
    plt.plot(X,X4,label='4x',linestyle='dotted')
    plt.legend()      
    plt.show() 
    
def affiche_complexite_3(Tableau,fn):
    C = []
    C2 = []
    X = range(1,520)
    
    T = Tableau()
    somme = cnt = 0
    for i in X:
        cnt = fn(T,i)
        somme += cnt
        C.append(cnt)
        C2.append(somme / i)
    
    plt.title("Dernière insertion")
    plt.plot(X,C,label='écritures')
    plt.plot(X,X,label='linéaire',linestyle='dotted')
    plt.legend()    
    plt.show() 
    
def affiche_complexite_4(Tableau,fn):

    C = []
    C2 = []
    X = range(1,520)

    T = Tableau()
    somme = cnt = 0
    for i in X:
        cnt = fn(T,i)
        somme += cnt
        C.append(cnt)
        C2.append(somme / i)

    XlogX = [ x*np.log2(x) for x in X ]

    X1 = [1]*len(X)
    X2 = [2]*len(X)
    X3 = [3]*len(X)

    plt.title("Moyenne des insertions")
    plt.plot(X,C2,label='écritures')
    plt.plot(X,X2,label='const 2',linestyle='dotted')
    plt.plot(X,X3,label='const 3',linestyle='dotted')
    plt.legend()

    plt.show() 