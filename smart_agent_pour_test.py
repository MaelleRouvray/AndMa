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
        self.player_name = player_name or "SmartAgent"

    def _get_action_space(self):
        """Accede a l'espace d'action seulement quand c'est necessaire."""
        return self.env.action_space(self.env.agents[0])

    def choose_action(self, board, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
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
        winning_move = self._find_winning_move(board, valid_actions, channel=0)
        if winning_move is not None:
            return winning_move

        # Rule 2: Block opponent
        blocking_move = self._find_winning_move(board, valid_actions, channel=1)
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
        Check if placing a piece at (row, col) would create 4 in a row.
        
        Note: Cette fonction suppose que le pion est déjà placé sur 'board' à (row, col).
        """
        # Directions: (Horizontal, Vertical, Diag /, Diag \)
        # Le sens opposé est vérifié en utilisant -dir_row et -dir_col
        directions = [(0, 1), (1, 0), (-1, 1), (1, 1)] 
        
        row_init = row
        col_init = col

        for dir_row, dir_col in directions:
            longueur = 1 # Le pion actuel (placé à row_init, col_init) compte pour 1

            # 1. Compter dans la direction positive (dir_row, dir_col)
            r = row_init + dir_row
            c = col_init + dir_col
            
            while 0 <= r < 6 and 0 <= c < 7 and board[r, c, channel] == 1:
                longueur += 1
                r += dir_row
                c += dir_col

            # 2. Compter dans la direction négative (opposée)
            # Démarrer à 1 pas dans la direction opposée
            r = row_init - dir_row 
            c = col_init - dir_col
            
            # Continuer l'itération dans la direction opposée
            while 0 <= r < 6 and 0 <= c < 7 and board[r, c, channel] == 1:
                longueur += 1
                r -= dir_row 
                c -= dir_col

            if longueur >= 4:
                return True
        
        return False


    def _find_winning_move(self, board, valid_actions, channel):
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
            row = self._get_next_row(board,col)
            if row is None:
                continue
            simulated_board=board.copy() #on simule une copie du palteau pour placer un pion et voir si le placement permet de gagner
            simulated_board[row, col, channel] = 1
            if self._check_win_from_position(simulated_board,row,col,channel):
                return col
        return None
            