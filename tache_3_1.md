Décomposition de l'implémentation de l'agent :
Un agent doit choisir quelle colonne jouer. Décomposez cela en sous-tâches :

1- Analyse des entrées : Quelles informations l'agent reçoit-il ?
2- Détection des coups valides : Comment déterminez-vous quelles colonnes sont jouables ?
3- Sélection du coup : Quel algorithme utiliserez-vous pour choisir un coup ?
4- Sortie : Que doit retourner l'agent ?



1- Information reçues par l'agent : l'état actuel du plateau donc les deux matrices observations (6x7x2), 

2- Colonnes jouables : grâce à action_mask, qui permet de dire quels coups sont valides ou non

3- Choix du coup à jouer : par les algorithmes: 
- Agent le plus simple possible
- Légèrement plus intelligent - évite les coups invalides
- Cherche des opportunités immédiates
- Jeu défensif
- Positionnement stratégique
- Algorithmes avancés

4- Sortie : le coup à effectuer et donc la matrice des observations mise à jour avec le cas de victoire éventuelle
