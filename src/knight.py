def knightMoves(board, turn):
    moves = {}
    if turn == 1:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and "wn" in board[row][col]:
                    foundMoves = []
                    piece = board[row][col]
                    if row + 2 in range(0, 8):
                        #bottom moves
                        if col - 1 in range(0, 8):
                            if board[row + 2][col - 1] == 0 or board[row + 2][col - 1][0] == "b":
                                foundMoves.append((row + 2, col - 1))
                        if col + 1 in range(0, 8):
                            if board[row + 2][col + 1] == 0 or board[row + 2][col + 1][0] == "b":
                                foundMoves.append((row + 2, col + 1))
                    if row - 2 in range(0, 8):
                        #top moves
                        if col - 1 in range(0, 8):
                            if board[row - 2][col - 1] == 0 or board[row - 2][col - 1][0] == "b":
                                foundMoves.append((row - 2, col - 1))
                        if col + 1 in range(0, 8):
                            if board[row - 2][col + 1] == 0 or board[row - 2][col + 1][0] == "b":
                                foundMoves.append((row - 2, col + 1))
                    if col + 2 in range(0, 8):
                        #right moves
                        if row - 1 in range(0, 8):
                            if board[row - 1][col + 2] == 0 or board[row - 1][col + 2][0] == "b":
                                foundMoves.append((row - 1, col + 2))
                        if row + 1 in range(0, 8):
                            if board[row + 1][col + 2] == 0 or board[row + 1][col + 2][0] == "b":
                                foundMoves.append((row + 1, col + 2))
                    if col - 2 in range(0, 8):
                        #left moves
                        if row - 1 in range(0, 8):
                            if board[row - 1][col - 2] == 0 or board[row - 1][col - 2][0] == "b":
                                foundMoves.append((row - 1, col - 2))
                        if row + 1 in range(0, 8):
                            if board[row + 1][col - 2] == 0 or board[row + 1][col - 2][0] == "b":
                                foundMoves.append((row + 1, col - 2))
                    moves[piece] = foundMoves
    if turn == 2:
        for row in range(0, 8):
            for col in range(0, 8):
                if type(board[row][col]) == str and "bn" in board[row][col]:
                    foundMoves = []
                    piece = board[row][col]
                    if row + 2 in range(0, 8):
                        #bottom moves
                        if col - 1 in range(0, 8):
                            if board[row + 2][col - 1] == 0 or board[row + 2][col - 1][0] == "w":
                                foundMoves.append((row + 2, col - 1))
                        if col + 1 in range(0, 8):
                            if board[row + 2][col + 1] == 0 or board[row + 2][col + 1][0] == "w":
                                foundMoves.append((row + 2, col + 1))
                    if row - 2 in range(0, 8):
                        #top moves
                        if col - 1 in range(0, 8):
                            if board[row - 2][col - 1] == 0 or board[row - 2][col - 1][0] == "w":
                                foundMoves.append((row - 2, col - 1))
                        if col + 1 in range(0, 8):
                            if board[row - 2][col + 1] == 0 or board[row - 2][col + 1][0] == "w":
                                foundMoves.append((row - 2, col + 1))
                    if col + 2 in range(0, 8):
                        #right moves
                        if row - 1 in range(0, 8):
                            if board[row - 1][col + 2] == 0 or board[row - 1][col + 2][0] == "w":
                                foundMoves.append((row - 1, col + 2))
                        if row + 1 in range(0, 8):
                            if board[row + 1][col + 2] == 0 or board[row + 1][col + 2][0] == "w":
                                foundMoves.append((row + 1, col + 2))
                    if col - 2 in range(0, 8):
                        #left moves
                        if row - 1 in range(0, 8):
                            if board[row - 1][col - 2] == 0 or board[row - 1][col - 2][0] == "w":
                                foundMoves.append((row - 1, col - 2))
                        if row + 1 in range(0, 8):
                            if board[row + 1][col - 2] == 0 or board[row + 1][col - 2][0] == "w":
                                foundMoves.append((row + 1, col - 2))
                    moves[piece] = foundMoves
    return moves