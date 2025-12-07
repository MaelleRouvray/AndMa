"""
Minimax agent with alpha-beta pruning
"""

import numpy as np
import random


class MinimaxAgent:
    """
    Agent using minimax algorithm with alpha-beta pruning
    """

    def __init__(self, env, depth=4, player_name=None):
        """
        Initialize minimax agent

        Parameters:
            env: PettingZoo environment
            depth: How many moves to look ahead
            player_name: Optional name
        """
        self.env = env
        self.action_space = env.action_space(env.agents[0])
        self.depth = depth
        self.player_name = player_name or f"Minimax(d={depth})"


    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose action using minimax algorithm
        """
        valid_actions = [i for i, valid in enumerate(action_mask) if valid == 1]

        best_action = None
        best_value = float('-inf')

        # Try each valid action
        for action in valid_actions:
            # Simulate the move
            new_board = self._simulate_move(observation, action, channel=0)

            # Evaluate using minimax (opponent's turn, so minimizing)
            value = self._minimax(new_board, self.depth - 1, float('-inf'), float('inf'), False)

            if value > best_value:
                best_value = value
                best_action = action

        return best_action if best_action is not None else random.choice(valid_actions)


    def _minimax(self, board, depth, alpha, beta, maximizing):
        """
        Minimax algorithm with alpha-beta pruning

        Parameters:
            board: Current board state
            depth: Remaining depth to search
            alpha: Best value for maximizer
            beta: Best value for minimizer
            maximizing: True if maximizing player's turn

        Returns:
            float: evaluation score
        """
        # TODO: Implement minimax
        # Base cases:
        if depth == 0 or self._check_win(board, 0) or self._check_win(board, 1):
            channel = 0
            if maximizing:
                channel = 1
            return self._evaluate_position(board, channel)

        # Recursive case:
        valid_col = self._get_valid_moves(board)

        if maximizing:
            val = float('-inf')
            channel = 0

            for col in valid_col:
                new_board = self._simulate_move(board, col, 0)
                val = max(val, self._minimax(new_board, depth-1, alpha, beta, False))
                alpha = max(val, alpha)
                #prune
                if alpha >= beta:
                    break
            return val
        
        else:
            val = float('inf')
            channel = 1

            for col in valid_col:
                new_board = self._simulate_move(board, col, channel)
                val = min(val, self._minimax(new_board, depth-1, alpha, beta, True))
                beta = min(beta, val)
                #prune:
                if alpha >= beta:
                    break
            return val
      
        

    def _simulate_move(self, board, col, channel):
        """
        Simulate placing a piece without modifying original board

        Parameters:
            board: Current board (6, 7, 2)
            col: Column to play
            channel: 0 for current player, 1 for opponent

        Returns:
            new_board: Copy of board with move applied
        """
        # Copy board 
        copy_board = board.copy()
    
        # Find next available row in column
        for row in range(5,-1,-1):
            if copy_board[row, col, 1] == 0 and copy_board[row, col, 0] == 0 :
                # Place piece
                copy_board[row, col, channel] = 1
                # Return new board
                return copy_board
        return copy_board #cas où la colonne est pleine: on retourne le même jeu


    def _get_valid_moves(self, board):
        """
        Get list of valid column indices

        Returns:
            list of valid columns
        """
        valid_columns=[i for i in range(7) if board[0, i, 0] == 0 and board[0, i, 1] == 0]
        return valid_columns




    def _check_win(self, board, channel):
        """
        Check if player has won

        Returns:
            bool: True if won
        """
        
        longueur = 0
        #en ligne
        for i in range(6):
            for j in range(7):
                if board[i, j, channel] == 1:
                    longueur += 1
                else:
                    longueur = 0
                if longueur == 4:
                    return True
            longueur = 0
        
        #en colonnes:
        for j in range(7):
            for i in range(6):            
                if board[i, j, channel] == 1:
                    longueur += 1
                else:
                    longueur = 0
                if longueur == 4:
                    return True
            longueur = 0
        
        #diagonale /:
        for i in range(3): #on ne regarde pas après la ligne 2 et colonne 3 car dans la boucle on sortirait du plateau avant d'avoir 4 pions alignés
            for j in range(4):
                sum = 0
                k = 0
                while board[i+k, j+k, channel] == 1 and i+k < 6 and j+k < 7:
                    sum += 1
                    k += 1
                    if sum == 4:
                        return True
                    
        #diagonale \:
        for i in range(3): 
            for j in range(3, 7):
                sum = 0
                k = 0
                while board[i-k, j+k, channel] == 1 and i+k < 6 and j-k>=0:
                    sum += 1
                    k += 1
                    if sum == 4:
                        return True
        return False