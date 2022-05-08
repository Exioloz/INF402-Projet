# Projet Futoshiki SAT-Solveur en INF402

### Dépendances nécessaires  : 

Pour pouvoir utiliser le programme, il est nécessaire d'avoir les dépendances suivantes : 

* Python 3.x
* numpy
* pysat

### Mode d'emploi du programme :  

Pour pouvoir exécuter le programme, taper la commande suivante : 

    python3 main.py <nom_du_fichier>

Le fichier passé en argument doit **obligatoirement** se trouver dans le dossier *Futoshiki_in* du dossier. 

Après exécution du fichier , le fichier CNF sortant est placé dans le dossier CNF_out et le fichier contenant le Futoshiki résolu sera placé dans le dossier *Futoshiki_out*.

Le fichier CNF est normalement utilisé par le SAT-solveur inclus dans le programme (inclus à l'aide de la bibliothèque pysat). Ce fichier peut être également utilisé par
d'autre SAT-solveurs, comme celui-ci (en ligne) : 

[https://jgalenson.github.io/research.js/demos/minisat.html]
