# Activité 1
## Partie 1
### Tache 1.1

1/ Les dimensions d'un plateau: 3D array (6,7,2) (rows, cols, channels)

2/ Un agent gagne la partie s'il aligne 4 de ses pions, il gagne 1 point et son adversaire perd un point ou si l'adversaire fait une action illégale: il gagne 0 point et l'advesaire perd un point.

3/ Si le plateau est remplit sans gagnant les deux gagnent 0 point (il ne se passe rien).

4/ Un joueur ne peut pas ajouter de pion dans un colonne pleine.

5/ Le jeu se termine quand:
    Un joueur a 4 pions alignés 
    ou
    les 7 colonnes sont remplies .


### Tache 1.2
1/  
| _ | _ | _ | _ | _ | _ | _ |  
| _ | _ | _ | _ | _ | _ | _ |  
| _ | _ | _ | X | _ | _ | _ |  
| _ | _ | 0 | X | _ | _ | _ |  
| _ | 0 | X | X | _ | _ | _ |     verticale  
| 0 | X | O | X | O | _ | _ |   

| _ | _ | _ | _ | _ | _ | _ |  
| _ | _ | _ | _ | _ | _ | _ |  
| _ | _ | _ | X | _ | _ | _ |  
| _ | _ | 0 | X | _ | _ | _ |  
| _ | 0 | X | 0 | _ | _ | _ |     horizontale  
| 0 | X | X | X | X | _ | _ |   

| _ | _ | _ | _ | _ | _ | _ |   
| _ | X | _ | _ | _ | _ | _ |  
| _ | 0 | X | X | _ | _ | _ |  
| _ | 0 | 0 | X | _ | _ | _ |      diagonale gauche  
| _ | 0 | X | X | X | _ | _ |  
| 0 | X | 0 | X | 0 | 0 | _ |   

| _ | _ | _ | _ | _ | _ | _ |    
| _ | _ | _ | _ | _ | _ | _ |  
| _ | _ | _ | X | X | _ | _ |  
| _ | _ | 0 | X | 0 | _ | _ |  
| _ | 0 | X | 0 | 0 | _ | _ |     diagonale droite  
| 0 | X | 0 | X | 0 | _ | _ |   

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

# Partie 2 
### Tache2.1
1/ 'player_0' et 'player_1'
2/ action est un set d'entiers de 0 à 6. Elle représente les colonnes où le jeton peut être placé. ?
3/ env.agent_iter():
   env.step(action):
4/ 
5/ 
6/ action_mask regroupe les actions disponibles pour l'agent. C'est un vecteur binaire où chaque valeur indique si l'action est légale ou non. Si ce n'est pas le tour de l'agent, le vecteur est zéro. Il permet à l'agent de ne pas faire d'action illégale et donc de perdre des points.

### Tache 2.2
1/ Le tableau d'observation est un tableau 2 * 6 lignes * 7 colonnes.
2/ premier tableau de 6*7 représente le plateau du joueur player_0 et le deuxième tableau représente le plateau du joueur player_1
3/ 0 ou 1?

### Tache 2.3
```from pettingzoo.classic import connect_four_v3
import numpy as np

def print_board(observation):
    """
    Print a human-readable version of the board

    observation: numpy array of shape (6, 7, 2)
        observation[:,:,0] = current player's pieces
        observation[:,:,1] = opponent's pieces
    """

    jeu_play=observation[:,:,0]
    jeu_adv=observation[:,:,1]

    n,m=jeu_play.shape
    rep=""
    for i in range(n):
        for j in range(m):
            if jeu_play[i,j]==1:
                rep+="X "
            elif jeu_adv[i,j]==1:
                rep+="O "
            else:
                rep+=". "
        print(rep)
        rep=""
    # TODO: Implement this function
    # Hint: Loop through rows and columns
    # Use symbols like 'X', 'O', and '.' for current player, opponent, and empty
    pass
# Test your function
env = connect_four_v3.env()
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        break

    print(f"\nAgent: {agent}")
    print_board(observation['observation'])

    # Make a few moves to see the board change
    env.step(3)
    if agent == env.agents[0]:
        break

env.close()```
