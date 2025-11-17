# AndMa
ConnectFour

# Activité 1
## Partie 1
tache 1.1

1/ Les dimensions d'un plateau: 3D array (6,7,2) (rows, cols, channels)

2/ Un agent gagne la partie s'il aligne 4 de ses pions, il gagne 1 point et son adversaire perd un point ou si l'adversaire fait une action illégale: il gagne 0 point et l'advesaire perd un point.

3/ Si le plateau est remplit sans gagnant les deux gagnent 0 point (il ne se passe rien).

4/ Un joueur ne peut pas ajouter de pion dans un colonne pleine.

5/ Le jeu se termine quand:
    Un joueur a 4 pions alignés 
    ou
    les 7 colonnes sont remplies .


tache 1.2
1/
|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|
|_|_|_|X|_|_|_|
|_|_|O|X|_|_|_|
|_|O|X|X|_|_|_|     verticale
|O|X|O|X|O|_|_| 

|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|
|_|_|_|X|_|_|_|
|_|_|O|X|_|_|_|
|_|O|X|O|_|_|_|     horizontale
|O|X|X|X|X|_|_| 

|_|_|_|_|_|_|_|  
|_|X|_|_|_|_|_|
|_|0|X|X|_|_|_|
|_|0|O|X|_|_|_|     diagonale gauche
|_|O|X|X|X|_|_|
|O|X|O|X|O|0|_| 

|_|_|_|_|_|_|_|  
|_|_|_|_|_|_|_|
|_|_|_|X|X|_|_|
|_|_|O|X|0|_|_|
|_|O|X|O|0|_|_|     diagonale droite
|O|X|O|X|O|_|_| 

2/ 8 directions doivent être vérifiées pour une victoire.

3/
choisir un point de départ 
while "longueur < 4" et "toutes les directions non étudiées":
    longueur=1
    choisir une direction parmi les 8 (ou moins si on est sur un bord) possibles
    avancer dans cette direction à partir du point de départ
    while "la case est occupée par un pion du même type":
        longueur +=1
    prendre la direction opposée 
    avancer dans cette direction à partir du point de départ
    while "la case est occupée par un pion du même type":
        longueur +=1
if longueur==4 :
    return "victoire"
else:
    return "pas  encore de victoire"


    # AndMa
ConnectFour
