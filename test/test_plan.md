## 1.1 Que tester?

# Tests fonctionnels:

-> lui proposer des cas limites: 3 pions alignés dans une colonne pleine, ...
-> vérifier à chaque coup si l'action choisie est dans le masque d'action
-> vérifier:
        - si toutes les colonnes sont pleines que le jeu a été arrêté
        - si victoire le jeu s'arrête

# Tests de performance: 
    -> ajouter un chronomètre au moment du tour de l'agent et une fois que l'agent a placé son pion (utiliser time.time()) <0.1 seconde
    -> utiliser tracemalloc pour mesurer l'utilisation de la mémoire < 10 MB

# Tests stratégiques:
    -> lancer un grand nombre de parties et vérifier que la proportion de victoire est supérieure à 80% .
    -> détecte une victoire immédiate
    -> pré-enregistrer un certain nombre d'états comme "menaces évidentes" et vérifier que l'agent bloque bien la menace (principalement 3 pions alignés)
    -> l'agent choisit la victoire plutôt que de bloquer son adversaire quand les deux cas se présentent simultanément

# Critère de succès
    -> au moins 80% de réussite en moyenne
    -> utilisation de moins de 10 MB de mémoire
    -> temps moyen de décision < 0.1 seconde à chaque coup

# Conception de cas test
    État du plateau :
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        X X X . . . .  <- Ligne du bas, 3 alignés

    Attendu : L'agent joue la colonne 3 pour gagner

    
    État du plateau :
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . . . . . .
        O O O . . . .  <- L'adversaire a 3 alignés

    Attendu : L'agent joue la colonne 3 pour bloquer

    
    État du plateau :
        . . . . . . .
        . . . . . . .
        . . . . . . .
        . . X 0 . . .
        0 X X X . . .
        X 0 0 0 . . .   <- 3 alignés en ligne pour l'adversaire, 3 alignés en diagonale pour l'agent 
    
    Attendu: le joueur joue la colonne 3


    État du plateau :
        . X . . . . .
        . X . . . . .
        . X . . . . .
        . 0 . . . . .
        . X . . . . .
        . 0 . . . . . 
   
    Attendu :  l'agent ne joue pas la colonne 1


    État du plateau :
        X 0 X 0 X X 0
        0 0 x 0 X X X
        X 0 X 0 X 0 0
        0 X 0 X 0 X 0
        0 X 0 X X X 0
        0 0 0 X 0 X X  <- le plateau est complet

    Attendu : La partie s'arrête: égalité