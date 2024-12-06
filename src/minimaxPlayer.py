from gameTree import *
from player import *
import random


class MinimaxPlayer:
    def __init__(self, ply, turn):
        self.ply = ply
        self.turn = turn
        self.kingMoved = False
    
    def __repr__(self):
        return "Computer"

    def chooseMove(self, board):
        tree = ChessTree(self.ply, board, self.turn)
        current_board = tuple([tuple(row) for row in board])
        current_board_node = tree.nodes[current_board]

        minimax_values_of_children = {}
        for child in current_board_node.children:
            tupled_child = tuple([tuple(row) for row in child.board])
            minimax_values_of_children[tupled_child] = child.minimaxValue
#get a dictionary of all of the minimax values of the children with the board as the key^

        if self.turn == 1:
            board_with_best_move = None
            values_list = list(minimax_values_of_children.values())#all the minimax values of the children
            if values_list == []:
                return "L 1 2"
            key_list = list(minimax_values_of_children.keys())#the children boards
            max_value = max(values_list)#max minimax value
            indexes = []
            for index in range(0, len(values_list)):
                if values_list[index] == max_value:
                    indexes.append(index)
            index = random.choice(indexes)#get the index of the maximum minimax value
            board_with_best_move = key_list[index]#get the board with the highest minimax values

        elif self.turn == 2:
            board_with_best_move = None
            values_list = list(minimax_values_of_children.values())
            if values_list == []:
                return "L 1 2"
            key_list = list(minimax_values_of_children.keys())
            min_value = min(values_list)
            indexes = []
            for index in range(0, len(values_list)):
                if values_list[index] == min_value:
                    indexes.append(index)
            index = random.choice(indexes)
            board_with_best_move = key_list[index]#see above, but with minimum minimax value

        for i in range(0, 8):
            for j in range(0, 8):
                if board[i][j] != board_with_best_move[i][j]:
                    if type(board_with_best_move[i][j]) == str:
                        return board_with_best_move[i][j] + f" {i} {j}"

class ManualPlayer:
    def __init__(self, turn):
        self.turn = turn
        self.kingMoved = False

    def chooseMove(self, board): 
        x = input("please input your move in form: piece row col")
        return x

    def __repr__(self):
        return "Player" + str(self.turn)