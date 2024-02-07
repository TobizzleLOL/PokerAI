import random

class Player:
    def __init__(self, _name):
        self.name = _name           #creating the Player
        self.cards = []
        self.stack = 1000
        self.bet = 0
        self.active = True

    def decide(self, _pot, _toCall):        #this method returns the action random // cant fold for practical debugging
        match random.randint(0,10):
            case 1:
                return 'raise'
            case _:
                return 'call'