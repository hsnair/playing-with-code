"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for row in board:
        for cell in row:
            if cell == X:
                count_x += 1
            elif cell == X:
                count_o += 1
    
    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_spaces = set()
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                empty_spaces.add((i, j))
    
    return empty_spaces


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, column = action

    if board[row][column] != EMPTY:
        raise ValueError("Invalid move")
    
    new_board = board
    new_board[row][column] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    board_len = len(board)

    for my_player in [X, O]:
        # Horizontal check for winner
        if [my_player] * board_len in board:
            return my_player
        
        # Vertical check for winner
        for i in range(board_len):
            if [my_player] * board_len == [row[i] for row in board]:
                return my_player
        
        # Diagonal check for winner
        if [my_player] * board_len == [board[i][i] for i in range(board_len)]:
            return my_player
        elif [my_player] * board_len == [board[i][-i-1] for i in range(board_len)]:
            return my_player
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    my_winner = winner(board)
    
    if my_winner == X:
        return 1
    elif my_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # current_player = player(board)
    # empty_spaces = actions(board)
    # num_turns_left = len(empty_spaces)

    # for action in empty_spaces:
    #     new_board = result(board, action)
    #     if terminal(new_board):
    #         return action
    
    current_player = player(board)

    if terminal(board):
        return utility(board)
    
    if current_player == X:
        v = -1 * 10^6
        for action in actions(board):
            v = max(v, minimax(result(board, action)))
        return v
    else:
        v = 1 * 10^6
        for action in actions(board):
            v = min(v, minimax(result(board, action)))
        return v
    

    