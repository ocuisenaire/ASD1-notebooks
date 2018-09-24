def convertir_en_texte(B):
    r = [ ( i + B.debut ) % B.capacite for i in range(B.taille)]
    s = "" if B.taille > 0 else "Rien"
    for i in r:
        s += "{0} ".format(B.data[i])
    s = "{:<12} | ".format(s)
    s += "debut: {0} | taille: ({1}/{2}) | ".format(B.debut,B.taille,B.capacite)
    s += "{}".format(B.data)

    return s 