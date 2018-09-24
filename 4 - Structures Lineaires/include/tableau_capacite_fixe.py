def convertir_en_texte(T):
    return "T({1}/{2}): {0}".format(T.data,T.taille,T.capacite)

def taille(T): 
    return T.taille

def calcule_indice_insertion(T,indice):
    if indice < 0 : indice += T.taille
    if indice < 0 : return 0
    if indice > T.taille: return T.taille
    return indice

def calcule_indice(T,indice):
    return indice if indice >= 0 else indice + T.taille

def verifier_indice(T,indice):
    if indice < 0 or indice >= T.taille: 
        raise IndexError("")
        
def verifier_place_disponible(T,besoin = 1):
    if T.taille + besoin > T.capacite:
        raise Exception("capacité insuffisante")
           
def lire_valeur_indice(T,indice): 
    indice = calcule_indice(T,indice)
    verifier_indice(T,indice)
    
    return T.data[indice]
    
def ecrire_valeur_indice(T,indice,value): 
    indice = calcule_indice(T,indice)
    verifier_indice(T,indice)

    T.data[indice] = value
        
def inserer_en_queue(T,valeur): 
    verifier_place_disponible(T)
    
    T.data[T.taille] = valeur
    T.taille += 1
    
def supprimer_en_queue(T):
    verifier_indice(T,0)
    
    T.taille -= 1
    T.data[T.taille] = None
    
def inserer_en_position(T,indice,valeur):
    indice = calcule_indice_insertion(T,indice) 
    verifier_place_disponible(T)
    
    for i in range(T.taille,indice,-1):
        T.data[i] = T.data[i-1]
    T.data[indice] = valeur
    T.taille += 1
    
def supprimer_en_position(T,indice = -1):
    indice = calcule_indice(T,indice)
    verifier_indice(T,indice)
    
    for i in range(indice,T.taille):
        T.data[i] = T.data[i+1]
    T.taille -= 1
    T.data[T.taille] = None
    
