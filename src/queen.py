from bishop import *
from rook import *

def queenMoves(board, turn):
    moves = {}
    if turn == 1:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and "wq" in board[row][col]:
                    #this one just combines the helpers from rook moves and bishop moves
                    piece = board[row][col]
                    diags = getDiagonal(board, row, col)
                    sides = getSides(board, row, col)
                    se, sw, ne, nw = sortDiags(diags, row, col)
                    left, right, up, down = sortSides(sides, row, col)
                    checkedDiags = checkDiag(se, board, turn) + checkDiag(sw, board, turn) + checkDiag(ne, board, turn) + checkDiag(nw, board, turn)
                    checkedSides = checkLine(left, board, turn) + checkLine(right, board, turn) + checkLine(up, board, turn) + checkLine(down, board, turn)
                    moves[piece] = checkedDiags + checkedSides
    if turn == 2:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and "bq" in board[row][col]:
                    piece = board[row][col]
                    diags = getDiagonal(board, row, col)
                    sides = getSides(board, row, col)
                    se, sw, ne, nw = sortDiags(diags, row, col)
                    left, right, up, down = sortSides(sides, row, col)
                    checkedDiags = checkDiag(se, board, turn) + checkDiag(sw, board, turn) + checkDiag(ne, board, turn) + checkDiag(nw, board, turn)
                    checkedSides = checkLine(left, board, turn) + checkLine(right, board, turn) + checkLine(up, board, turn) + checkLine(down, board, turn)
                    moves[piece] = checkedDiags + checkedSides
    return moves
