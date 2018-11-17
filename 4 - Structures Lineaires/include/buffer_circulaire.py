def convertir_en_texte(B):
    r = [ ( i + B.debut ) % B.capacite for i in range(B.taille)]
    s = "" 
    for i in r:
        s += "{0} ".format(B.data[i])
    for i in range(B.capacite - B.taille):
        s += "  ";
        
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