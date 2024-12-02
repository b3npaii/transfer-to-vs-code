import copy

from bishop import *
from king import *
from knight import *
from pawn import *
from queen import *
from rook import *

class Queue:
    def __init__(self, contents=None):
        if contents is None:
            self.contents = []
        else:
            self.contents = contents

    def enqueue(self, item_to_queue):
        self.contents.append(item_to_queue)

    def dequeue(self):
        return self.contents.pop(0)

class Node:
    def __init__(self, board, turn, ply):
        self.board = board
        self.winner = None
        self.turn = turn
        self.legalMoves = {}
        self.findLegalMoves()
        self.children = []
        self.parent = None
        self.ply = ply
        self.minimaxValue = self.findMinimaxValue()

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
        king = kingMoves(self.board, self.turn, False)
        self.legalMoves.update(king)
        if check:
            self.legalMovesInCheck()
        self.checkGameOver()

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
                        newMoves += self.legalMoves[newPiece]
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
                    self.turn = turn
        self.legalMoves = copiedMoves
        self.board = copiedBoard
        self.turn = turn

    def checkCheck(self):
        altMoves = {}
        otherPlayer = self.turn + 1
        if otherPlayer == 3:
            otherPlayer = 1
        altMoves.update(pawnMoves(self.board, otherPlayer))
        altMoves.update(knightMoves(self.board, otherPlayer))
        altMoves.update(bishopMoves(self.board, otherPlayer))
        altMoves.update(rookMoves(self.board, otherPlayer))
        altMoves.update(queenMoves(self.board, otherPlayer))
        altMoves.update(kingMoves(self.board, otherPlayer, False))
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

    def makeMove(self, board, piece, move):
        if piece in self.legalMoves and move in self.legalMoves[piece]:
            #make sure the move is legal
            #special case for castling
            if move == "castleShort":
                if self.turn == 1:
                    board[7][6] = "wk"
                    board[7][5] = "wr2"
                    self.board[7][7] = board[7][4] = 0
                else:
                    board[0][6] = "bk"
                    board[0][5] = "br2"
                    board[0][7] = board[0][4] = 0
            elif move == "castleLong":
                if self.turn == 1:
                    board[7][2] = "wk"
                    board[7][3] = "wr1"
                    board[7][0] = board[7][4] = 0
                else:
                    board[0][2] = "wk"
                    board[0][3] = "wr1"
                    board[0][0] = board[0][4] = 0
            elif "wp" in piece and move[0] == 0:
                self.promoteWhitePawn(piece, move)
            elif "bp" in piece and move[0] == 7:
                self.promoteBlackPawn(piece, move)
            else:
                #put the piece on the new spot and take it off the old one
                oldRow, oldCol = self.findPiece(piece, board)
                newRow, newCol = move
                board[newRow][newCol] = piece
                board[oldRow][oldCol] = 0
            return board

    def checkGameOver(self):
        allMoves = []
        for piece in self.legalMoves:
            allMoves += self.legalMoves[piece]
        if allMoves == []:
            self.gameOver = True
            if self.turn == 1:
                self.winner = 2
            else:
                self.winner = 1

    def findMinimaxValue(self):
        if self.winner != None:
            if self.winner == 2:
                return -1000000
            elif self.winner == 1:
                return 1000000
        score = 0
        pieceCounter = {1: 0, 2: 0}
        for row in self.board:
            for col in self.board:
                if col != 0:
                    if "w" in col:
                        pieceCounter[1] += 1
                    else:
                        pieceCounter[2] += 1
        if pieceCounter[1] > pieceCounter[2]:
            score += pieceCounter[1] - pieceCounter[2]
        else:
            score -= (pieceCounter[1] - pieceCounter[2])
        return score

class ChessTree:
    def __init__(self, ply, board, turn):
        self.cycles = 1
        self.ply = ply
        self.turn = turn
        if self.turn == 1:
            self.next = 2
        else:
            self.next = 1
        self.tree = self.generateTree(board)
        self.assignMinimaxValues(Node(board, 1, 1))

    def makeMove(self, board, piece, move, legalMoves):
        if piece in legalMoves and move in legalMoves[piece]:
            #make sure the move is legal
            #special case for castling
            if move == "castleShort":
                if self.turn == 1:
                    board[7][6] = "wk"
                    board[7][5] = "wr2"
                    self.board[7][7] = board[7][4] = 0
                else:
                    board[0][6] = "bk"
                    board[0][5] = "br2"
                    board[0][7] = board[0][4] = 0
            elif move == "castleLong":
                if self.turn == 1:
                    board[7][2] = "wk"
                    board[7][3] = "wr1"
                    board[7][0] = board[7][4] = 0
                else:
                    board[0][2] = "wk"
                    board[0][3] = "wr1"
                    board[0][0] = board[0][4] = 0
            elif "wp" in piece and move[0] == 0:
                self.promoteWhitePawn(piece, move)
            elif "bp" in piece and move[0] == 7:
                self.promoteBlackPawn(piece, move)
            else:
                #put the piece on the new spot and take it off the old one
                oldRow, oldCol = self.findPiece(piece, board)
                newRow, newCol = move
                board[newRow][newCol] = piece
                board[oldRow][oldCol] = 0
            return board

    def findPiece(self, piece, board):
        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] == piece:
                    return i, j

    def generateTree(self, board):
        first = Node(board, 1, 1)
        queue = Queue([first])
        self.root = first
        self.nodes = {tuple([tuple(row) for row in board]): first}
        
        while queue.contents != []:
            dequeued = queue.dequeue()
            if dequeued.ply > self.ply:
                break
            if dequeued.winner != None:
                continue

            board = dequeued.board
            moves = dequeued.legalMoves
            list_of_nodes = []

            for piece in moves:
                for move in moves[piece]:
                    copied_board = copy.deepcopy(board)
                    new_board = self.makeMove(copied_board, piece, move, moves)
                    tupled_board = tuple([tuple(row) for row in new_board])

                    new_node = Node(new_board, self.next, dequeued.ply + 1)
                    new_node.parent = dequeued
                    dequeued.children.append(new_node)

                    list_of_nodes.append(new_node)
                    self.nodes[tupled_board] = new_node


            for node in list_of_nodes:
                queue.enqueue(node)
            
        self.turn += 1
        if self.turn == 3:
            self.turn = 1
        self.next += 1
        if self.next == 3:
            self.next = 1
        self.cycles += 1

    def assignMinimaxValues(self, node):

        if node.children == []:
            node.minimax_value = node.findMinimaxValue()

        else:
            children_minimax_values = []

            for child in node.children:
                self.assignMinimaxValues(child)
                children_minimax_values.append(child.minimaxValue)

            if node.turn == 1:
                node.minimaxValue = max(children_minimax_values)
            else:
                node.minimaxValue = min(children_minimax_values)

        return node.minimaxValue
