from ete3 import Tree

from ete3 import Tree, TreeStyle, TextFace, add_face_to_node

ts = TreeStyle()
ts.show_leaf_name = False
ts.show_scale = False
ts.branch_vertical_margin = 15
def my_layout(node):
    F = TextFace(" " + node.name + " ", tight_text=False,fsize=20)
    add_face_to_node(F, node, column=0, position="branch-right")
ts.layout_fn = my_layout

def newick8_from_heap( T, i ):   
    s = ""
    if 2 * i + 1< len(T):
        s += "("
        if 2 * i + 2 < len(T):
            s += newick8_from_heap(T,2*i+2)
            s += ","
        s += newick8_from_heap(T,2*i+1)
        s += ")"
    s += "{0}".format(T[i])
    return s

def afficher_tas(R):
    n = newick8_from_heap(R,0)+";"
    t = Tree(n,format=8)
    display(t.render("%%inline", tree_style=ts))