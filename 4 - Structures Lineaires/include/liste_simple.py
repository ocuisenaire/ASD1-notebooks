def afficher_maillon(self):
    if self:
        return "{} → ".format(self.donnee) + afficher_maillon(self.suivant)
    else:
        return "⌀"
    
    
class Maillon:
    def __init__(self,valeur):
        self.donnee = valeur       
        self.suivant = None 
    __str__ = afficher_maillon 