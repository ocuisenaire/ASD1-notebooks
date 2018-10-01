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