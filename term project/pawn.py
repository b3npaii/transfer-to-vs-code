def pawnMoves(board, turn):
    moves = {}
    if turn == 1:
        for i in range(0, 8):
            for j in range(0, 8):
                if type(board[i][j]) == str and 'wp' in board[i][j]:
                    #checks if the front square is open
                    if board[i - 1][j] == 0:
                        moves[board[i][j]] = [(i - 1, j)]
                    if i == 6:
                        #checks if the pawn has moved yet to determine if it can move two squares
                        if board[i - 2][j] == 0 and board[i][j] in moves:
                            moves[board[i][j]].append((i - 2, j))
                    if j - 1 >= 0:
                        #checking pawn captures to the left
                        if type(board[i - 1][j - 1]) == str and "b" in board[i - 1][j - 1]:
                            if board[i][j] not in moves:
                                moves[board[i][j]] = [(i - 1, j - 1)]
                            else:
                                moves[board[i][j]].append((i - 1, j - 1))
                    if j + 1 <= 7:
                        #pawn captures to the right
                        if type(board[i - 1][j + 1]) == str and "b" in board[i - 1][j + 1]:
                            if board[i][j] not in moves:
                                moves[board[i][j]] = [(i - 1, j + 1)]
                            else:
                                moves[board[i][j]].append((i - 1, j + 1))
                    #need to add in clause for promotion
                    
    if turn == 2:
        for i in range(0, 8):
            for j in range(0, 8):
                if type(board[i][j]) == str and 'bp' in board[i][j]:
                    if board[i + 1][j] == 0:
                        moves[board[i][j]] = [(i + 1, j)]
                    if i == 1:
                        if board[i + 2][j] == 0 and board[i][j] in moves:
                            moves[board[i][j]].append((i + 2, j))
                    if j - 1 >= 0:
                        if type(board[i + 1][j - 1]) == str and "w" in board[i + 1][j - 1]:
                            if board[i][j] not in moves:
                                moves[board[i][j]] = [(i + 1, j - 1)]
                            else:
                                moves[board[i][j]].append((i + 1, j - 1))
                    if j + 1 <= 7:
                        if type(board[i + 1][j + 1]) == str and "w" in board[i + 1][j + 1]:
                            if board[i][j] not in moves:
                                moves[board[i][j]] = [(i + 1, j + 1)]
                            else:
                                moves[board[i][j]].append((i + 1, j + 1))
                        # need to add en passante at some point
    return moves