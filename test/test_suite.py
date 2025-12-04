# tests stratégiques :

import smart_agent as sm_ag
import test_smart_agent as test_sm_ag
import pytest
from pettingzoo.classic import connect_four_v3

@pytest.fixture

def agent():
    env=connect_four_v3.env(render_mode="human")
    return sm_ag.SmartAgent(env)


# gagne contre un agent aléatoire : 
# -> lancer un grand nombre de parties et vérifier que la proportion de victoire est supérieure à 80% .
def test_multi_play(agent):
    assert agent.test_sm_ag.multi_play(100)[2] >= 80

# bloque les menaces évidentes 
# pré-enregistrer un certain nombre d'états comme "menaces évidentes" et vérifier que l'agent bloque bien la menace (principalement 3 pions alignés)
def test_bloc_menace(agent): 
    obs = {"observations" : np.zeros(6,7,2)}
    obs["observations"][0,0,1]= 1 
    obs["observations"][0,1,1]= 1 
    obs["observations"][0,2,1]= 1 
    action_mask = [0,1,2,3,4,5,6]
    action = agent.choose_action(obseravtion = obs, action_mask = action_mask)
    assert action == 3

# détecte une victoire immédiate 
def test_victoire_immediate(agent):
    obs = {"observations" : np.zeros(6,7,2)}
    obs["observations"][0,0,0]= 1 
    obs["observations"][0,1,0]= 1 
    obs["observations"][0,2,0]= 1 
    action_mask = [0,1,2,3,4,5,6]
    action = agent.choose_action(observation=obs, action_mask=action_mask)
    assert action == 3

# choisit la victoire plutot que bloquer l'adversaire quand les 2 cas se présentent en même temps
def test_victoire_over_block(agent):
    obs = {"observations" : np.zeros(6,7,2)}
    obs["observations"][0,0,0]= 1 
    obs["observations"][1,1,0]= 1 
    obs["observations"][2,2,0]= 1
    obs["observations"][1,2,0]= 1 
    obs["observations"][1,3,0]= 1 
    obs["observations"][0,1,1]= 1 
    obs["observations"][0,2,1]= 1 
    obs["observations"][0,3,1]= 1 
    obs["observations"][2,3,1]= 1 
    action_mask = [0,1,2,3,4,5,6]
    action = agent.choose_action(observation=obs, action_mask=action_mask)
    assert action == 3