import pandas as pd
from bishop import *
from king import *
from knight import *
from pawn import *
from player import *
from queen import *
from rook import *
import copy


class Game:
    def __init__(self, player1, player2, log=True):
        self.log = log
        self.players = [player1, player2]
        self.board = self.generateBoard()
        if self.log == True:
            self.printBoard()
        self.turn = 1
        self.gameOver = False
        self.winner = None
        self.findLegalMoves()

    def printBoard(self):
        print(pd.DataFrame(self.board))

    def generateBoard(self):
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[6] = ["wp" + str(i + 1) for i in range(8)]
        board[1] = ["bp" + str(i + 1) for i in range(8)]
        board[7] = ["wr1", "wn1", "wb1", "wq", "wk", "wb2", "wn2", "wr2"]
        board[0] = ["br1", "bn1", "bb1", "bq", "bk", "bb2", "bn2", "br2"]
        return board

    def makeMove(self, piece, move, check=True):
        if piece in self.legalMoves and move in self.legalMoves[piece]:
            #make sure the move is legal
            #special case for castling
            if move == "castleShort" and not self.checkCheck():
                if self.turn == 1:
                    self.board[7][6] = "wk"
                    self.board[7][5] = "wr2"
                    self.board[7][7] = self.board[7][4] = 0
                else:
                    self.board[0][6] = "bk"
                    self.board[0][5] = "br2"
                    self.board[0][7] = self.board[0][4] = 0
            elif move == "castleLong" and not self.checkCheck():
                if self.turn == 1:
                    self.board[7][2] = "wk"
                    self.board[7][3] = "wr1"
                    self.board[7][0] = self.board[7][4] = 0
                else:
                    self.board[0][2] = "wk"
                    self.board[0][3] = "wr1"
                    self.board[0][0] = self.board[0][4] = 0
            elif "wp" in piece and move[0] == 0:
                self.promoteWhitePawn(piece, move)
            elif "bp" in piece and move[0] == 7:
                self.promoteBlackPawn(piece, move)
            else:
                #put the piece on the new spot and take it off the old one
                oldRow, oldCol = self.findPiece(piece)
                newRow, newCol = move
                self.board[newRow][newCol] = piece
                self.board[oldRow][oldCol] = 0
            if "k" in piece:
                self.players[self.turn - 1].kingMoved = True
            self.turn = [2, 1][self.turn - 1]
            if self.log == True:
                self.printBoard()
            self.findLegalMoves(check)
        else:
            if self.log:
                print("That's not a legal move! Try again.")

    def promoteWhitePawn(self, oldPiece, move):
        newPiece = "wq"
        counter = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if self.board[row][col] != 0 and newPiece in self.board[row][col]:
                    counter += 1
        oldRow, oldCol = self.findPiece(oldPiece)
        newRow, newCol = move
        if counter > 0:
            newPiece += str(counter + 1)
        self.board[newRow][newCol] = newPiece
        self.board[oldRow][oldCol] = 0

    def promoteBlackPawn(self, oldPiece, move):
        newPiece = "bq"
        counter = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if self.board[row][col] != 0 and newPiece in self.board[row][col]:
                    counter += 1
        oldRow, oldCol = self.findPiece(oldPiece)
        newRow, newCol = move
        if counter > 0:
            newPiece += str(counter + 1)
        self.board[newRow][newCol] = newPiece
        self.board[oldRow][oldCol] = 0

    def findPiece(self, piece):
        for i in range(0, 8):
            for j in range(0, 8):
                if self.board[i][j] == piece:
                    return i, j

    def checkCheck(self):
        altMoves = {}
        otherPlayer = [2, 1][self.turn - 1]
        altMoves.update(pawnMoves(self.board, otherPlayer))
        altMoves.update(knightMoves(self.board, otherPlayer))
        altMoves.update(bishopMoves(self.board, otherPlayer))
        altMoves.update(rookMoves(self.board, otherPlayer))
        altMoves.update(queenMoves(self.board, otherPlayer))
        altMoves.update(kingMoves(self.board, otherPlayer, self.players[self.turn - 1].kingMoved))
        allAltMoves = []
        for piece in altMoves:
            allAltMoves += altMoves[piece]
        for i in range(0, len(allAltMoves)):
            if type(allAltMoves[i]) == tuple:
                x, y = allAltMoves[i]
                if self.board[x][y] != 0 and "k" in self.board[x][y]:
                    if self.turn == 1:
                        if self.board[x][y] == "wk":
                            return True
                    else:
                        if self.board[x][y] == "bk":
                            return True
        return False

    def findLegalMoves(self, check=True):
        self.legalMoves = {}
        pawns = pawnMoves(self.board, self.turn)
        self.legalMoves.update(pawns)
        knights = knightMoves(self.board, self.turn)
        self.legalMoves.update(knights)
        bishop = bishopMoves(self.board, self.turn)
        self.legalMoves.update(bishop)
        rook = rookMoves(self.board, self.turn)
        self.legalMoves.update(rook)
        queen = queenMoves(self.board, self.turn)
        self.legalMoves.update(queen)
        king = kingMoves(self.board, self.turn, self.players[self.turn - 1].kingMoved)
        self.legalMoves.update(king)
        if check:
            self.legalMovesInCheck()
        self.checkGameOver()
        if self.log and not self.gameOver:
           print(self.legalMoves)

    def legalMovesInCheck(self):
        copiedBoard = copy.deepcopy(self.board)
        copiedMoves = dict(self.legalMoves)
        turn = int(str(self.turn))
        if self.checkCheck():
            for piece in copiedMoves:
                i = 0
                while i < len(copiedMoves[piece]):
                    move = copiedMoves[piece][i]
                    #if still in check after the move, take it out of legal moves
                    #save state the board and revert after checking
                    self.makeMove(piece, move, False)
                    newMoves = []
                    triggered = False
                    for newPiece in self.legalMoves:
                        for move in self.legalMoves[newPiece]:
                            if type(move) == tuple:
                                newMoves.append(move)
                    for x, y in newMoves:
                        if self.board[x][y] != 0 and "k" in self.board[x][y]:
                            if move in copiedMoves[piece]:
                                copiedMoves[piece].remove(move)
                                triggered = True
                    if not triggered:
                        i += 1
                    #need to make them copies or else it changes copiedBoard, etc (i forgot this and was stuck on this for an hour)
                    self.legalMoves = copiedMoves.copy()
                    self.board = copy.deepcopy(copiedBoard)
                    self.turn = int(str(turn))
        self.legalMoves = copiedMoves
        self.board = copiedBoard
        self.turn = turn

    def checkGameOver(self):
        allMoves = []
        for piece in self.legalMoves:
            allMoves += self.legalMoves[piece]
        if allMoves == []:
            self.gameOver = True
            if self.turn == 1:
                self.winner = self.players[1]
            else:
                self.winner = self.players[0]
            # print("The game is over! The winner is ", end="")
            # print(self.winner)

    def chooseMove(self):
        pieceAndMove = self.players[self.turn - 1].chooseMove(self.board)
        splitted = pieceAndMove.split()
        return splitted[0], tuple([int(splitted[1]), int(splitted[2])])

