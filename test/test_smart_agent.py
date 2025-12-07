import smart_agent as sm_ag
import numpy as np
import pytest
from pettingzoo.classic import connect_four_v3

@pytest.fixture
def agent():
    """Fixture qui fournit une instance de SmartAgent à chaque test"""
    env=connect_four_v3.env(render_mode="human")
    return sm_ag.SmartAgent(env)

def test_get_valid_actions(agent):
    """Test de la fonction _get_valid_actions"""
    assert agent._get_valid_actions([1, 1, 1, 1, 1, 1, 1]) == [0, 1, 2, 3, 4, 5, 6]
    assert agent._get_valid_actions([0, 1, 0, 1, 0, 1, 0]) == [1, 3, 5]


def test_find_winning_move(agent):
    """Test de la fonction _find_winning_move"""
    observation = {"observation": np.zeros((6, 7, 2))}
    #pions du joueur 0
    observation["observation"][0, 2,0]=1 
    observation["observation"][0, 4,0]=1
    observation["observation"][1, 2,0]=1
    
    valid_actions = [0, 1, 2, 3, 4, 5, 6]
    channel=0
    #cas pas de victoire
    assert agent._find_winning_move(observation, valid_actions,channel)==None
    #cas victoire:
    observation2 =  {"observation": np.zeros((6, 7, 2))}
    #pions du joueur 0
    observation2["observation"][5, 2, 0] = 1
    observation2["observation"][4, 2, 0] = 1
    observation2["observation"][3, 2, 0] = 1
    """État du plateau :
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . . X . . . .
            . . X . . . .
            . . X . . . . 
    """
    valid_actions2 = [0, 1, 2, 3, 4, 5, 6]
    channel2=0
    assert agent._find_winning_move(observation2, valid_actions2, channel2)==2

def test_get_next_row(agent):
    """Test de la fonction _get_next_row"""
    board = np.zeros((6, 7, 2))
    assert agent._get_next_row(board, 3) == 5
    board[5, 3, 0] = 1
    assert agent._get_next_row(board, 3) == 4

def test_check_win_from_position(agent):
    """Test de la fonction _check_win_from_position"""
    #cas pas de victoire
    board = np.zeros((6, 7, 2))
    board[0,1,0]=1
    board[0,3,0]=1
    """État du plateau :
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . X . X . . .
    """
    row=0
    col=4
    channel=0
    assert agent._check_win_from_position(board,row , col, channel)==False

    #cas 2: victoire horizontale
    board2 = np.zeros((6, 7, 2))
    board2[0,1,0]=1
    board2[0,2,0]=1
    board2[0,3,0]=1

    """État du plateau :
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . X X X . . .
    """
    assert agent._check_win_from_position(board2,row , col, channel)==True

    #cas victoire verticale
    board3 = np.zeros((6, 7, 2))
    board3[0,1,0]=1
    board3[1,1,0]=1
    board3[2,1,0]=1

    """État du plateau :
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . X . . . . .
            . X . . . . .
            . X . . . . .
    """
    row3=3
    col3=1
    assert agent._check_win_from_position(board3 ,row3 , col3, channel)==True

    #cas victoire diagonale /
    board4 = np.zeros((6, 7, 2))
    board4[0,0,0]=1
    board4[0,1,1]=1
    board4[0,2,0]=1
    board4[0,3,1]=1
    board4[1,1,0]=1
    board4[1,2,1]=1
    board4[1,3,1]=1
    board4[2,2,0]=1
    board4[2,3,1]=1

    """État du plateau :
            . . . . . . .
            . . . . . . .
            . . . . . . .
            . . X 0 . . .
            . X 0 0 . . .
            X 0 X 0 . . .
    """
    row4=3
    col4=3
    assert agent._check_win_from_position(board4 ,row4 , col4, channel)==True
    
    #cas victoire diagonale \
    board5 = np.zeros((6, 7, 2))
    board5[0,0,1]=1
    board5[0,1,1]=1
    board5[0,2,1]=1
    board5[0,3,0]=1
    board5[1,0,1]=1
    board5[1,1,1]=1
    board5[1,2,0]=1
    board5[2,0,0]=1
    board5[2,1,0]=1
    """État du plateau :
            . . . . . . .
            . . . . . . .
            . . . . . . .
            X X . . . . .
            0 0 X . . . .
            0 0 0 X . . .
    """
    col5=0
    row5=3
    assert agent._check_win_from_position(board5 ,row5 , col5, channel)==True