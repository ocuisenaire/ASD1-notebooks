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

