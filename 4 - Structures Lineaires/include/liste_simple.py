def afficher_maillon(self):
    if self:
        return "{} → ".format(self.donnee) + afficher_maillon(self.suivant)
    else:
        return "⌀"
    
def to_string(L):
    return afficher_maillon(L)
    
class Maillon:
    def __init__(self,valeur):
        self.donnee = valeur       
        self.suivant = None 
    __str__ = afficher_maillon 