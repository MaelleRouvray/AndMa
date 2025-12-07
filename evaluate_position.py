def has_won(board,channel):
    nb_row = 6
    nb_col = 7
    directions = [(0,1),(1,0),(-1,1),(1,1)]
    for row in range(nb_row):
        for col in range(nb_col):
            for dr, dc in directions :
                lim_row = row + dr*3  
                lim_col = col + dc*3
                if 0 <= lim_row < nb_row and 0 <= lim_col < nb_col : 
                    window = [board[row + dr*i,col + dc*i,channel] for i in range(4)]
                    if sum(window) == 4 :
                        return True

    return False



def count_three_in_row(board,channel):
    nb_row = 6
    nb_col = 7
    directions = [(0,1),(1,0),(-1,1),(1,1)]
    count = 0
    for row in range(nb_row):
        for col in range(nb_col):
            for dr, dc in directions :
                lim_row = row + dr*3  
                lim_col = col + dc*3
                if 0 <= lim_row < nb_row and 0 <= lim_col < nb_col : 
                    window_player = [board[row + dr*i,col + dc*i,channel] for i in range(4)]
                    window_opponent =[board[row + dr*i,col + dc*i,1 - channel] for i in range(4)]
                    if sum(window_player) == 3 and sum(window_opponent) == 0:
                        count += 1
    return count




def count_two_in_row(board,channel):
    nb_row = 6
    nb_col = 7
    directions = [(0,1),(1,0),(-1,1),(1,1)]
    count = 0
    for row in range(nb_row):
        for col in range(nb_col):
            for dr, dc in directions :
                lim_row = row + dr*3  
                lim_col = col + dc*3
                if 0 <= lim_row < nb_row and 0 <= lim_col < nb_col : 
                    window_player = [board[row + dr*i,col + dc*i,channel] for i in range(4)]
                    window_opponent =[board[row + dr*i,col + dc*i,1 - channel] for i in range(4)]
                    if sum(window_player) == 2 and sum(window_opponent) <= 1:
                        count += 1
    return count



def count_pieces_in_center(board,channel):
    nb_row = 6
    count = 0
    for row in range(nb_row) :
        if board[row,3,channel] == 1 : 
            count += 1

    return count











def evaluate_position(board, player_channel):
    """
    Evaluate board position from player's perspective

    Returns:
        float: positive = good for player, negative = bad
    """
    score = 0

    # Check for wins
    if has_won(board, player_channel):
        return 10000

    if has_won(board, 1 - player_channel):
        return -10000

    # Count 3-in-a-row patterns (without the 4th piece blocked)
    score += count_three_in_row(board, player_channel) * 5

    # Count 2-in-a-row patterns
    score += count_two_in_row(board, player_channel) * 2

    # Prefer center positions
    score += count_pieces_in_center(board, player_channel) * 3

    return score