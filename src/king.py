def kingMoves(board, turn, moved):
    if turn == 1:
        moves = []
        for row in range(0, 8):
            for col in range(0, 8):
                if board[row][col] == "wk":
                    if row - 1 in range(0, 8):
                        #check above the king
                        if col - 1 in range(0, 8):
                            if board[row - 1][col - 1] == 0 or board[row - 1][col - 1][0] == "b":
                                moves.append((row - 1, col - 1))
                        if board[row - 1][col] == 0 or board[row - 1][col][0] == "b":
                            moves.append((row - 1, col))
                        if col + 1 in range(0, 8):
                            if board[row - 1][col + 1] == 0 or board[row - 1][col + 1][0] == "b":
                                moves.append((row - 1, col + 1))
                    if row + 1 in range(0, 8):
                        #checks below the king
                        if board[row + 1][col - 1] == 0 or board[row + 1][col - 1][0] == "b":
                                moves.append((row + 1, col - 1))
                        if board[row + 1][col] == 0 or board[row + 1][col][0] == "b":
                            moves.append((row + 1, col))
                        if col + 1 in range(0, 8):
                            if board[row + 1][col + 1] == 0 or board[row + 1][col + 1][0] == "b":
                                moves.append((row + 1, col + 1))
                    if col + 1 in range(0, 8):
                        #check to the right of the king
                        if board[row][col + 1] == 0 or board[row][col + 1][0] == "b":
                            moves.append((row, col + 1))
                    if col - 1 in range(0, 8):
                        #checks to the left of the king
                        if board[row][col - 1] == 0 or board[row][col - 1][0] == "b":
                            moves.append((row, col - 1))
                    if moved == False:
                        #checks for castling
                        if board[7][5] == 0 and board[7][6] == 0 and board[7][7] == "wr2":
                            moves.append("castleShort")
                        if board[7][0] == "wr1" and board[7][1] == 0 and board[7][2] == 0 and board[7][3] == 0:
                            moves.append("castleLong")
        return {"wk": moves}
    elif turn == 2:
        moves = []
        for row in range(0, 8):
            for col in range(0, 8):
                if board[row][col] == "bk":
                    if row - 1 in range(0, 8):
                        if col - 1 in range(0, 8):
                            if board[row - 1][col - 1] == 0 or board[row - 1][col - 1][0] == "w":
                                moves.append((row - 1, col - 1))
                        if board[row - 1][col] == 0 or board[row - 1][col][0] == "w":
                            moves.append((row - 1, col))
                        if col + 1 in range(0, 8):
                            if board[row - 1][col + 1] == 0 or board[row - 1][col + 1][0] == "w":
                                moves.append((row - 1, col + 1))
                    if row + 1 in range(0, 8):
                        if board[row + 1][col - 1] == 0 or board[row + 1][col - 1][0] == "w":
                                moves.append((row + 1, col - 1))
                        if board[row + 1][col] == 0 or board[row + 1][col][0] == "w":
                            moves.append((row + 1, col))
                        if col + 1 in range(0, 8):
                            if board[row + 1][col + 1] == 0 or board[row + 1][col + 1][0] == "w":
                                moves.append((row + 1, col + 1))
                    if col + 1 in range(0, 8):
                        if board[row][col + 1] == 0 or board[row][col + 1][0] == "w":
                            moves.append((row, col + 1))
                    if col - 1 in range(0, 8):
                        if board[row][col - 1] == 0 or board[row][col - 1][0] == "w":
                            moves.append((row, col - 1))
                    if moved == False:
                        if board[0][5] == 0 and board[0][6] == 0 and board[0][7] == "br2":
                            moves.append("castleShort")
                        if board[0][0] == "br1" and board[0][1] == 0 and board[0][2] == 0 and board[0][3] == 0:
                            moves.append("castleLong")
        return {"bk": moves}

