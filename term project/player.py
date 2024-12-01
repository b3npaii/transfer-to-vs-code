class Player:
    def __init__(self, turn):
        self.turn = turn
        self.kingMoved = False

    def chooseMove(self, board):
        return 42

    def __repr__(self):
        return "player " + str(self.turn)
