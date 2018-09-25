import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def grapheComplexite(func,N,title):
    X = range(2,N)
    XF = [ np.math.factorial(x) for x in X ]

    C = []
    for n in X:
        TAB = np.random.uniform(0,1,n)
        C.append(func(TAB,n))

    plt.semilogy(X,C,label=title)
    plt.semilogy(X,XF,label='n!')
    plt.legend()
    plt.title('Complexité')
    plt.show()

    i = len(X)-1
    print('Echanges pour {0} éléments: {1}'.format(X[i],C[i]))
    print('Factorielle({0}) :          {1}'.format(X[i],XF[i]))
    print('Rapport C({0})/({0}!-1):      {1}'.format(X[i],C[i]/(XF[i]-1)))


def affichageHanoi(Towers,title=None):
    with plt.xkcd():
        
        L = len(Towers[0]) + len(Towers[1]) + len(Towers[2])

        fig = plt.figure()
        ax = fig.add_axes((0,0,1,0.1*L))
        
        for d in range(0,L+1):
            for i,T in enumerate(Towers):
                for j,t in enumerate(T):
                    if d == t:
                        ax.bar(i,j+1,d/L)

        ax.spines['right'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.set_xticks([0, 1, 2])
        ax.set_xlim([-0.5, 2.5])
        ax.set_ylim([0, L])
        ax.set_xticklabels(['T1', 'T2', 'T3'])
        ax.set_yticks([])
        if title:
            plt.title(title)

    plt.show()