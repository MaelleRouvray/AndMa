from pettingzoo.classic import connect_four_v3
import numpy as np

def print_board(observation):
    """
    Print a human-readable version of the board

    observation: numpy array of shape (6, 7, 2)
        observation[:,:,0] = current player's pieces
        observation[:,:,1] = opponent's pieces
    """
    # TODO: Implement this function
    # Hint: Loop through rows and columns
    # Use symbols like 'X', 'O', and '.' for current player, opponent, and empty
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

env.close()