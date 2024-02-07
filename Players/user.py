class Player:
    def __init__(self, _name):
        self.name = _name
        self.cards = []
        self.stack = 1000
        self.bet = 0
        self.active = True

    def decide(self, stage, board):
        return input('what to do?')