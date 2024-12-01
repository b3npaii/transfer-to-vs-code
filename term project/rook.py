#get the board values on the cross centered at the rook
def getSides(board, row, col):
    sides = []
    for i in range(row + 1, 8):
        sides.append((i, col))
    for i in range(0, row):
        sides.append((i, col))
    for i in range(col + 1, 8):
        sides.append((row, i))
    for i in range(0, col):
        sides.append((row, i))
    return sides

#sort the sides to left, right, above, and below the rook
def sortSides(sides, row, col):
    left, right, up, down = [], [], [], []
    for x, y in sides:
        if x < row:
            left.append((x, y))
        elif x > row:
            right.append((x, y))
        elif y > col:
            down.append((x, y))
        elif y < col:
            up.append((x, y))
    return left[::-1], right, up[::-1], down

#check the line for legal moves and get rid of illegal moves
#function needs the lines to be radiating outward from the rook to work, which is why we reverse left and up in sortSides
def checkLine(line, board, turn):
    newLine = []
    if turn == 1:
        for x, y in line:
            if board[x][y] == 0:
                newLine.append((x, y))
            elif type(board[x][y]) == str:
                #if there is a piece blocking the rest of the line is not legal, so the function returns here
                if "b" in board[x][y] and "w" not in board[x][y]:
                    newLine.append((x, y))
                return newLine
    elif turn == 2:
        for x, y in line:
            if board[x][y] == 0:
                newLine.append((x, y))
            elif type(board[x][y]) == str:
                if "w" in board[x][y]:
                    newLine.append((x, y))
                return newLine
    return newLine


def rookMoves(board, turn):
    moves = {}
    if turn == 1:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and 'wr' in board[row][col]:
                    #finding the white rooks in the board
                    piece = board[row][col]
                    sides = getSides(board, row, col)
                    left, right, up, down = sortSides(sides, row, col)
                    #gets all possible moves then adds the legal ones to the dict
                    moves[piece] = checkLine(left, board, turn)
                    moves[piece] += checkLine(right, board, turn)
                    moves[piece] += checkLine(up, board, turn)
                    moves[piece] += checkLine(down, board, turn)
    if turn == 2:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and 'br' in board[row][col]:
                    piece = board[row][col]
                    sides = getSides(board, row, col)
                    left, right, up, down = sortSides(sides, row, col)
                    moves[piece] = checkLine(left, board, turn)
                    moves[piece] += checkLine(right, board, turn)
                    moves[piece] += checkLine(up, board, turn)
                    moves[piece] += checkLine(down, board, turn)
    return moves
