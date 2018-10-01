from ete3 import Tree

from ete3 import Tree, TreeStyle, TextFace, add_face_to_node

ts = TreeStyle()
ts.show_leaf_name = False
ts.show_scale = False
ts.branch_vertical_margin = 15
def my_layout(node):
    F = TextFace(" " + node.name + " ", tight_text=False,fsize=15)
    add_face_to_node(F, node, column=0, position="branch-right")
ts.layout_fn = my_layout

def newick8_from_binary_tree(R):
    s = ""
    if R:
        if R.gauche or R.droite:
            s += "("
            s += newick8_from_binary_tree(R.droite)
            s += ","
            s += newick8_from_binary_tree(R.gauche)
            s += ")"
        s += "{0}".format(R.data)
    else:
        s += "⌀"
    return s

def afficher_arbre_binaire(R):
    n = newick8_from_binary_tree(R)+";"
    # print(n)
    t = Tree(n,format=8)
    display(t.render("%%inline", tree_style=ts))
    
# Arbres AVL   

class Node:
    def __init__(self,val):
        self.data = val
        self.droite = None
        self.gauche = None
        self.hauteur = 1

def hauteur(R):
    return R.hauteur if R else 0

def calculer_hauteur(R):
    if R:
        R.hauteur = max( hauteur(R.gauche), hauteur(R.droite)) + 1

def equilibre(R):    
    return hauteur(R.gauche) - hauteur(R.droite) if R else 0

def rotation_droite(x):
    y = x.gauche
    x.gauche = y.droite
    y.droite = x
    calculer_hauteur(x)
    calculer_hauteur(y)
    return y

def rotation_gauche(x):
    y = x.droite
    x.droite = y.gauche
    y.gauche = x
    calculer_hauteur(x)
    calculer_hauteur(y)
    return y

def equilibrage(R):
    assert(R != None)
    eq = equilibre(R)
    if eq < -1:
        if equilibre(R.droite) > 0:
            R.droite = rotation_droite( R.droite )
        R = rotation_gauche(R)    
    elif eq > 1:
        if equilibre(R.gauche) < 0:
            R.gauche = rotation_gauche(R.gauche)
        R = rotation_droite(R)
    else:
        calculer_hauteur(R)
    return R

def inserer(R,val,equilibrer = True):
    if R == None:
        return Node(val)
    else:
        if val < R.data:
            R.gauche = inserer(R.gauche,val,equilibrer)
        elif val > R.data:
            R.droite = inserer(R.droite,val,equilibrer)
        else: # val == R.data
            pass
        return equilibrage(R) if equilibrer else R
      
def meilleurs_cas_AVL():
    R = None
    for i in range(1:16): 
        R = inserer(R,i)
    return R

def pire_cas_AVL():
    R = None
    R = inserer(R,3)
    R = inserer(R,2)
    R = inserer(R,5)
    R = inserer(R,4)
    R = inserer(R,1)
    R = inserer(R,6)
    R = inserer(R,7)
    return R