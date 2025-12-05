## Tests stratégiques :

import smart_agent as sm_ag
from test_smart_VS_random import multi_play
import numpy as np
import pytest
from pettingzoo.classic import connect_four_v3

@pytest.fixture
def agent():
    """Fixture qui fournit une instance de SmartAgent à chaque test"""
    env=connect_four_v3.env(render_mode="None")
    env.reset()
    return sm_ag.SmartAgent(env)



def test_taux_victoire(agent):
    """Test qui vérifie si smart agent gagne contre un agent aléatoire
        La proportion de victoire de smart agent doit être supérieure à 80%
    """
    num_games = 20
    vic0, vic1, coups, egalite = multi_play(num_games)
    assert vic0 + vic1 + egalite == num_games  # toutes les parties se terminent

    taux_vic1 = vic1 / num_games
    assert taux_vic1 >= 0.8
    

def test_block_menace(agent): 
    """ Test qui vérifie si smart agent bloque les menaces évidentes """
    obs = {"observation" : np.zeros((6,7,2))}
    board = obs["observation"]
    board[5,0,1]= 1 
    board[5,1,1]= 1 
    board[5,2,1]= 1 
    action_mask = [1,1,1,1,1,1,1]
    action = agent.choose_action(observation = obs, action_mask = action_mask)
    assert action == 3


def test_victoire_immediate(agent):
    """ Teste si smart agent détecte une victoire immédiate """
    obs = {"observation" : np.zeros((6,7,2))}
    board = obs["observation"]
    board[5,0,0]= 1 
    board[5,1,0]= 1 
    board[5,2,0]= 1 
    action_mask = [1,1,1,1,1,1,1]
    action = agent.choose_action(observation=obs, action_mask=action_mask)
    assert action == 3

def test_victoire_over_block(agent):
    """ Teste si smart agent choisit la victoire plutot que le blocage de l'adversaire 
        si les deux situations se présentent
    """ 
    obs = {"observation" : np.zeros((6,7,2))}
    board = obs["observation"]
    board[5,0,0]= 1 
    board[4,1,0]= 1 
    board[3,2,0]= 1
    board[4,2,0]= 1 
    board[4,3,0]= 1 
    board[5,1,1]= 1 
    board[5,2,1]= 1 
    board[5,3,1]= 1 
    board[4,0,1]= 1
    board[3,3,1]= 1 
    action_mask = [1,1,1,1,1,1,1]
    action = agent.choose_action(observation=obs, action_mask=action_mask)
    assert action == 3