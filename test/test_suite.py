import pytest
import numpy as np
from pettingzoo.classic import connect_four_v3
import time
import tracemalloc
import random_agent as rd_ag
import smart_agent as sm_ag
#from test_smart_agent import multi_play
from test_smart_VS_random import multi_play

@pytest.fixture
def agent():
    """Fixture qui fournit une instance de SmartAgent à chaque test"""
    env=connect_four_v3.env(render_mode="None")
    env.reset()
    return sm_ag.SmartAgent(env)


# tests fonctionnels

def test_choix_dans_mask_action(agent):
    """
    Test si le choix de l'agent est bien dans mask_action
    """
    obs = {"observation" : np.zeros((6,7,2))}
    board = obs["observation"]
    board[5,0,1]=1
    board[5,1,0]=1
    board[4,1,1]=1
    board[4,0,0]=1
    board[3,1,1]=1
    board[2,1,0]=1
    board[1,1,1]=1
    board[0,1,0]=1
    board[5,2,1]=1
    board[4,2,0]=1
    board[3,2,1]=1
    board[2,2,0]=1
    board[1,2,1]=1
    board[0,2,0]=1
    action_mask = [1,0,0,1,1,1,1]
    action=agent.choose_action(observation=obs, action_mask = action_mask)
    assert (action != 1) and (action != 2)



def test_game_stops_on_full_board(pettingzoo_env_available=True):
    """
    Test si le jeu s'arrête lorsque la grille est pleine
    """

    env = connect_four_v3.env(render_mode=None)
    env.reset(seed=42)

    player0 = rd_ag.RandomAgent(env, "player_0")
    player1 = sm_ag.SmartAgent(env, "player_1")
    agents = {"player_0": player0, "player_1": player1}
    done = False

    for agent_name in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()
        if termination or truncation:
            done = True
            break
        action_mask = observation["action_mask"]
        if agent_name == "player_0":
            action = agents[agent_name].choose_action_manual(
                observation, reward, termination, truncation, info, action_mask
            )
        else:
            action = agents[agent_name].choose_action(
                observation, reward, termination, truncation, info, action_mask
            )
        env.step(action)

    env.close()
    assert done


#tests stratégiques

def test_taux_victoire(agent):
    """Test qui vérifie si smart agent gagne contre un agent aléatoire
        La proportion de victoire de smart agent doit être supérieure à 80%
    """
    num_games = 20
    vic0, vic1, coups, egalite, _ = multi_play(num_games)
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


# choisit la victoire plutot que bloquer l'adversaire quand les 2 cas se présentent en même temps
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


# test performance et critère de succès

def test_time_under_30(agent):
    """
    Vérifie que le temps de décision pour choisir une action est inférieur à 0.1 seconde
    """
    obs = {"observation" : np.zeros((6,7,2))}
    board = obs["observation"]
    board[5,0,0]= 1 
    board[5,1,0]= 1 
    board[5,2,0]= 1 
    action_mask = [1,1,1,1,1,1,1]
    t1=time.time()
    action = action = agent.choose_action(observation=obs, action_mask=action_mask)
    t2 = time.time() - t1
    assert t2 < 0.1

def test_memoire(agent):
    """
    Vérifie que la mémoire utilisée pour une partie est inférieure à 10MB
    """
    tracemalloc.start()
    before = tracemalloc.take_snapshot()
    multi_play(1)
    after = tracemalloc.take_snapshot()
    comp = before.compare_to(after, 'lineno')
    tot=0
    for stat in comp[:10]:
        tot+= stat.size
    assert tot < 10