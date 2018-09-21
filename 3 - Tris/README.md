
# Chapitre 3 - Tris

Dans ce chapitre nous passons en revue divers algorithmes de tri. Ils permettent d'ordonner le contenu d'un tableau (*) du plus petit au plus grand selon un critère donné. 

Comme le veut la tradition, nous commençons par présenter trois tris simples mais peu efficaces: le [tri à bulles](1a%20-%20Tri%20à%20Bulles.ipynb), le [tri par sélection](2%20-%20Tri%20Par%20Sélection.ipynb) et le [tri par insertion](3%20-%20Tri%20par%20Insertion.ipynb).

Nous profitons du tri à bulles pour présenter deux propriétés importantes des tris, leur [stabilité](1b%20-%20Stabilité.ipynb) et leur [complexité](1c%20-%20Complexité.ipynb). Ces propriétés sont ensuite analysées en détail dans le notebook de chaque tri. 

Nous poursuivons avec le [tri de Shell](4%20-%20Tri%20de%20Shell.ipynb), une variante du tri par insertion qui constitue notre premier tri réellement efficace. Vient ensuite le [tri par fusion](5%20-%20Tri%20par%20Fusion.ipynb), le plus efficace des tris stables présentés, et enfin nous finissons par le [tri rapide](6%20-%20Tri%20Rapide.ipynb), en moyenne le plus efficace.

Nous profitons du tri rapide pour présenter un algorithme proche, celui de [sélection rapide](7%20-%20Sélection%20rapide.ipynb), qui permet de trouver le nième plus petit élément d'un tableau en un temps linéaire. 

Enfin, nous concluons en discutant des fonctions de tri disponibles en [en C et C++](8%20-%20Tris%20en%20C%20et%20C%2B%2B.ipynb) via la librairie standard. 

Comme il n'est pas possible ici d'être exhaustif dans le cadre de ce cours, nous vous encourageons à feuilleter [Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm) pour avoir une idée de la diversité des approches possibles. Lors des laboratoires, vous aurez l'occasion d'en explorer d'autres comme le [tri comptage](https://fr.wikipedia.org/wiki/Tri_comptage). Notez aussi l'algorithme de tri utilisé par python: [Timsort](https://fr.wikipedia.org/wiki/Timsort). 

Notons que nous n'en aurons pas complètement fini avec les tris, au chapitre 4, nous nous intéresserons au tri de contenu stocké dans une liste chainée plutôt que dans un tableau. Nous introduirons aussi la notion de tas, qui nous permettra d'effectuer le [tri par tas](https://fr.wikipedia.org/wiki/Tri_par_tas) d'un tableau. 

Enfin, pour le plaisir, vous devriez aussi essayer 

* [xkcd: Ineffective Sorts](https://xkcd.com/1185/), expliqué [ici](https://www.explainxkcd.com/wiki/index.php/1185:_Ineffective_Sorts)
* [stacksort](https://gkoberger.github.io/stacksort/)
