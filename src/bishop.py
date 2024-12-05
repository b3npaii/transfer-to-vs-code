#returns everything on the two intersecting diagonals the bishop is on
def getDiagonal(board, row, col):
    i = 1
    length = range(0, len(board))
    diagonal = []
    while (row + i) < len(board) or (row - i) >= 0 or (col + i) < len(board) or (col - i) >= 0:
        if row + i in length and col + i in length:
            diagonal.append((row + i, col + i))
        if row + i in length and col - i in length:
            diagonal.append((row + i, col - i))
        if row - i in length and col + i in length:
            diagonal.append((row - i, col + i))
        if row - i in length and col - i in length:
            diagonal.append((row - i, col - i))
        i += 1
    return diagonal

#sorts the diagonals according to where they are relative to the bishop
def sortDiags(diagonals, row, col):
    se, sw, ne, nw = [], [], [], []
    for x, y in diagonals:
        if x > row and y > col:
            se.append((x, y))
        elif x < row and y > col:
            ne.append((x, y))
        elif x > row and y < col:
            sw.append((x, y))
        else:
            nw.append((x, y))
    return se, sw, ne, nw

#checks the diagonals for legal moves, similar to the rook move helper function logic
def checkDiag(diag, board, turn):
    newDiag = []
    for x, y in diag:
        if board[x][y] == 0:
            newDiag.append((x, y))
        elif type(board[x][y]) == str:
            if turn == 1:
                if board[x][y][0] == "b":
                    newDiag.append((x, y))
            elif turn == 2:
                if board[x][y][0] == "w":
                    newDiag.append((x, y))
            return newDiag
    return newDiag

def bishopMoves(board, turn):
    moves = {}
    if turn == 1:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and "wb" in board[row][col]:
                    #finds the white bishops on the board
                    piece = board[row][col]
                    diagonals = getDiagonal(board, row, col)
                    se, sw, ne, nw = sortDiags(diagonals, row, col)
                    #gets all possible moves and sorts them according to direction
                    moves[piece] = checkDiag(se, board, turn)
                    moves[piece] += checkDiag(sw, board, turn)
                    moves[piece] += checkDiag(nw, board, turn)
                    moves[piece] += checkDiag(ne, board, turn)
                    #adds all the legal moves to the dict
    if turn == 2:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and "bb" in board[row][col]:
                    piece = board[row][col]
                    diagonals = getDiagonal(board, row, col)
                    se, sw, ne, nw = sortDiags(diagonals, row, col)
                    moves[piece] = checkDiag(se, board, turn)
                    moves[piece] += checkDiag(sw, board, turn)
                    moves[piece] += checkDiag(nw, board, turn)
                    moves[piece] += checkDiag(ne, board, turn)
    return moves

