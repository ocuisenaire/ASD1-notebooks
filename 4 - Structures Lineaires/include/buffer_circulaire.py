def convertir_en_texte(B):
    r = [ ( i + B.debut ) % B.capacite for i in range(B.taille)]
    s = "" if B.taille > 0 else "Rien"
    for i in r:
        s += "{0} ".format(B.data[i])
    s = "{:<10} | ".format(s)
    s += "d: {0} | t/c: ({1}/{2}) | ".format(B.debut,B.taille,B.capacite)
    s += "{}".format(B.data)

    return s 

class BufferCirculaire:
    def __init__(self,capacite):
        self.data = [None]*capacite
        self.capacite = capacite
        self.taille = 0
        self.debut = 0
    
    __str__     = convertir_en_texte
    
def BufferDemo():
    B = BufferCirculaire(6)
    B.debut = 4
    B.taille = 5
    for i in range(B.taille):
        B.data[(B.debut + i) % B.capacite] = i*i
    return B