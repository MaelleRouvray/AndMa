"""
My Smart Agent for Connect Four

This agent uses rule-based heuristics to play strategically.
"""

import random


class SmartAgent:
    """
    A rule-based agent that plays strategically
    """

    def __init__(self, env, player_name=None):
        """
        Initialize the smart agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional name for the agent
        """
        self.env = env
        self.action_space = env.action_space(env.agents[0])
        self.player_name = player_name or "SmartAgent"

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose an action using rule-based strategy

        Strategy priority:
        1. Win if possible
        2. Block opponent from winning
        3. Play center if available
        4. Random valid move
        """
        # Get valid actions
        valid_actions = self._get_valid_actions(action_mask)

        # Rule 1: Try to win
        winning_move = self._find_winning_move(observation, valid_actions, channel=0)
        if winning_move is not None:
            return winning_move

        # Rule 2: Block opponent
        blocking_move = self._find_winning_move(observation, valid_actions, channel=1)
        if blocking_move is not None:
            return blocking_move

        # Rule 3: Prefer center
        if 3 in valid_actions:
            return 3

        # Rule 4: Random fallback
        return random.choice(valid_actions)

    def _get_valid_actions(self, action_mask):
        """
        Get list of valid column indices

        Parameters:
            action_mask: numpy array (7,) with 1 for valid, 0 for invalid

        Returns:
            list of valid column indices
        """
        valid_actions = []
        for i in range(len(action_mask)):
            if action_mask[i] == 1:
                valid_actions.append(i)
        return valid_actions

    def _find_winning_move(self, observation, valid_actions, channel):
        """
        Find a move that creates 4 in a row for the specified player

        Parameters:
            observation: numpy array (6, 7, 2) - current board state
            valid_actions: list of valid column indices
            channel: 0 for current player, 1 for opponent

        Returns:
            column index (int) if winning move found, None otherwise
        """
        # TODO: For each valid action, check if it would create 4 in a row
        # Hint: Simulate placing the piece, then check for wins
    
        for col in valid_actions:
            row = _get_next_row(self,observation,col)
            if _check_win_from_position(self,observation,row,col,channel):
                return col
        return None
            



    def _get_next_row(self, board, col):
        """
        Find which row a piece would land in if dropped in column col

        Parameters:
            board: numpy array (6, 7, 2)
            col: column index (0-6)

        Returns:
            row index (0-5) if space available, None if column full
        """
        for i in range(5,-1,-1):
            if board[i,col,0] == 0 and board[i,col,1] == 0 :
                return i
        return None

    def _check_win_from_position(self, board, row, col, channel):
        """
        Check if placing a piece at (row, col) would create 4 in a row

        Parameters:
            board: numpy array (6, 7, 2)
            row: row index (0-5)
            col: column index (0-6)
            channel: 0 or 1 (which player's pieces to check)

        Returns:
            True if this position creates 4 in a row/col/diag, False otherwise
        """
        # TODO: Check all 4 directions: horizontal, vertical, diagonal /, diagonal \
        # Hint: Count consecutive pieces in both directions from (row, col)
        # horizontal : board[row,col,channel] -> board[row,col+-1,channel]
        # vertical : board[row,col,channel] -> board[row+-1,col,channel]
        # diagonal / : board[row,col,channel] -> board[row+1,col+1,channel]
        #              board[row,col,channel] -> board[row-1,col-1,channel]
        # diagonal \ : board[row,col,channel] -> board[row+1,col-1,channel]
        #              board[row,col,channel] -> board[row-1,col+1,channel]
        col_init = col
        row_init = row
    
        # direction horizontale
        longueur = 1
        while board[row,col+1,channel] == 1:
            longueur += 1
            col = col+1
        col = col_init
        row = row_init
        while board[row,col-1,channel] == 1:
            longueur += 1
            col = col-1
        
        if longueur == 4:
            return True

        # direction verticale
        longueur = 1
        while board[row+1,col,channel] == 1:
            longueur += 1
            col = col+1
        col = col_init
        row = row_init
        while board[row-1,col,channel] == 1:
            longueur += 1
            col = col-1
        
        if longueur == 4:
            return True

        # direction diagonale /
        longueur = 1
        while board[row+1,col+1,channel] == 1:
            longueur += 1
            col = col+1
        col = col_init
        row = row_init
        while board[row-1,col-1,channel] == 1:
            longueur += 1
            col = col-1
        
        if longueur == 4:
            return True


        # direction diagonale \
        longueur = 1
        while board[row+1,col-1,channel] == 1:
            longueur += 1
            col = col+1
        col = col_init
        row = row_init
        while board[row-1,col+1,channel] == 1:
            longueur += 1
            col = col-1
        
        if longueur == 4:
            return True

        
        return False