# Problem 38
from copy import deepcopy

def queens_board(n):
    board = []
    for i in range(n):
        board.append([])
    for i in range(n):
        for j in range(n):
            board[i].append(True)
    for i in range(n):
        for j in range(n):
            copy_board = deepcopy(board)
            if board[i][j] is True:
                copy_board = place_piece(copy_board, i, j)

                

def place_piece(board, i, j):
    for a in range(len(board)):
        board[i][a] = False
        board[a][j] = False
    a = i
    b = j
    while a < len(board) and b < len(board):
        board[a][b] = False
        a += 1
        b += 1
    a = i
    b = j
    while a > -1 and b > -1:
        board[a][b] = False
        a -= 1
        b -= 1
    return board


