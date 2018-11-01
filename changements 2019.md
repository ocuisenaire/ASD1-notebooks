# Changements aux cours d'ASD1 de 2018 à 2019

La principale nouveauté est le passage de supports de cours 

* sous forme d'un powerpoint par chapitre
* mélangeant du pseudo-code et du code C++

à des supports 

* sous forme de jupyter notebooks 
* et de présentations reveal.js associées
* avec un notebook par sujet, une dizaine par chapitre
* en langage python pour expliquer les algorithmes et structures
* et en C++ pour l'utilisation des algorithmes et structures équivalentes la STL

Cette transition est complète pour les chapitres 3 à 6. Les chapitres 1 et 2 utilisent toujours des transparents powerpoints pour les présentations et des slideDocs pour le support écrit, avec quelques notebooks en soutien. 

## Chap. 1 - Introduction

L'introduction au pseudo-code est remplacée par une brève introduction à python. 

## Chap. 2 - Récursivité

La multiplication du paysan russe est présentée plus en détail. Précédemment le principe en était présenté uniquement pour le calcul des puissances, sans généralisation. Cela permet également de présenter l'algorithme asymptotiquement optimal en O(log n) pour Fibonacci plutôt que de se contenter de la version linéaire

## Chap. 3 - Tris

Le tri à bulles est présenté avant d'introduire les notions de stabilité et de complexité des tris. 

La notion de complexité spatiale est introduite. 

La description des algorithmes est plus progressive, par exemple en introduisant les boucles internes avant les doubles boucles dans les tri à bulle, par sélection et par insertion. 

Le présentation du tri de Shell est plus précise et actuelle concernant le choix de la séquence des valeurs de h. 

Pour le tri par fusion, la variante à deux tableaux est présentée. Elle divise par deux le nombre d'écriture dans les tableaux par rapport à celle de base. Nous omettons toujours la variante bottom-up. Les variantes en place sont signalées mais pas présentées. 

Pour le tri rapide, l'importance du choix du pivot, du traitement des valeurs égales au pivot, et de la dérécursification d'un des appels récursif est traité plus précisément. 

L'étude de la complexité des divers algorithmes est un peu plus détaillée avec une visualisation graphique pour chaque tri.

La présentation des tris en C et C++ est plus exhaustive, même si certaines fonctions sont juste citées et pas présentées en détail. Les présentations de std::sort, std::stable_sort, std::nth_element et std::partial_sort sont plus détaillées

## Chap. 4 - Structures linéaires

La présentation des tableaux est plus systématique, progressive et incrémentale, n'introduisant dans chaque notebook que les méthodes nouvelles n'existant pas dans le notebook précédent. 

La structure de buffer circulaire est introduite. 

La présentation des listes simplement chainées est entièrement ré-écrite, introduisant pas à pas la notion d'itérateur sur ces listes.

La présentation des listes doublement chainées est entièrement ré-écrite, en utilisant dès le début des itérateurs pour en écrire les méthodes 

La présentation du tri de listes est entièrement ré-écrite, en utilisant les itérateurs et en introduisant progressivement la méthode splice qui permet de déplacer les maillons de la chaine. 

La structure de deque est présentée en détail plutôt que simplement mentionnée. 

La présentation des tas introduit les fonctions parent et enfants pour simplifier le code. Elle est plus explicite sur le fait qu'un tas est un tableau et que la visualisation sous forme d'arbre binaire ne correspond pas à une structure d'arbre concrète.

Les TDA pile, file et file de priorité sont présentés ensemble et indépendamment de la STL. 

La présentation des structures linéaires de la STL est divisées en 3 parties: sequence containers, container adaptors et heaps. La réécriture de la présentations des listes chainées nous permet d'être ici plus précis sur les différentes méthodes offertes par la STL et sur la notion de validité des itérateurs. 

## Chap. 5 - Arbres

La présentation des arbres génériques et plus rigoureuse, chaque notion étant accompagnée de code la mettant en oeuvre, y compris pour les représentations linéaires indentée et imbriquée. 

Les algorithmes de création d'un arbre binaire à partir de deux de ses parcours sont présentés explicitement

L'utilisation d'arbres pour représenter les expressions arithmétiques est présentée plus en détail. Les algorithmes de création de l'arbre depuis l'expression sont tous fournis. 

La présentation des arbres binaires de recherche est divisée en 5 notebooks. 

Les TDA ensemble et tableau associatif sont présentés en tant que TDA et plus simplement via la STL en C++. 

Le TDA ensemble introduit les algorithmes d'union, d'intersection, de différence et d'inclusion. 

La présentation de std::set est plus précise. Elle distingue l'insertion normale en O(log n) de l'insertion avec indice en O(1), ainsi que les conséquences de cette distinction sur les complexités des autres opérations. 

La présentation de std::map est plus précise et montrant plus clairement sa parenté avec std::set et en détaillant plus exactement le fonctionnement de map::operator<

La présentation des fonctions set_union, set_intersection, set_difference et set_symmetric_difference est introduite comme mise en oeuvre du TDA ensemble. Elle permet de terminer la présentation des itérateurs de la STL avec inserter, back_inserter et front_inserter. 

## Chap. 6 - Graphes 

TBD
