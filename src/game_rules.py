

def create_board() -> list[list[int]]:
    """
    This function creates the game board

    :return: a 3x3 matrix filled with zeros
    """
    return [[0] * 3 for _ in range(3)]

def apply_move(board, move, x_player = True) -> list[list[int]]:
    """
    this function applies the move to the board

    :param board: a 3x3 matrix as the board
    :param move: an ordered pair of the move
    :param x_player: a boolean indicating if the player is X or O
    :return: the resulting board
    """
    if move is None:
        return board

    row, col = move

    if x_player:
        board[row][col] = 1
    else:
        board[row][col] = -1

    return board

def get_legal_moves(board) -> list[int]:
    """
    this function gets the legal moves

    :param board: a 3x3 matrix representing the board
    :return: a list of the legal moves in an ordered pair
    """
    moves = []

    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                moves.append((x,y))

    return moves

def win_check(board) -> int | None:
    """
    This function checks for a win, loss, or draw focused on x player (learner model)
    :param board: a 3x3 matrix representing the board
    :return: int value or None; representing the winning condition
    """
    x_player = 1
    o_player = -1

    for row in board:
        if row[0] == x_player and row[0] == row[1] == row[2]:
            return 1

        if row[0] == o_player and row[0] == row[1] == row[2]:
            return -1


    for col in range(3):
        if board[0][col] == x_player and board[0][col] == board[1][col] == board[2][col]:
            return 1

        if board[0][col] == o_player and board[0][col] == board[1][col] == board[2][col]:
            return -1

    # left diag
    if board[0][0] == x_player and board[0][0] == board[1][1] == board[2][2]:
        return 1

    if board[0][0] == o_player and board[0][0] == board[1][1] == board[2][2]:
        return -1

    # right diag
    if board[0][2] == x_player and board[0][2] == board[1][1] == board[2][0]:
        return 1

    if board[0][2] == o_player and board[0][2] == board[1][1] == board[2][0]:
        return -1

    #game still going
    for row in board:
        if 0 in row:
            return None

    return 0