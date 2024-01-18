import random

class Game():
    def __init__(self, *Players):
        self.Players = Players
        self.deck = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                     '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                     '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                     '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]
        self.board = []
        self.pot = 0
        self.blindsize = 2
        self.toCall = self.blindsize

    def start(self):
        self.blinds()
        self.deal()
        self.betround(2)
        self.flop()
        self.betround(0)
        self.turn()
        self.betround(0)
        self.river()
        self.betround(0)
        self.showdown()
    

    def blinds(self):
        self.Players[0].bet = 0.5 * self.blindsize
        self.Players[1].bet = 1.0 * self.blindsize


    def deal(self):
        for player in self.Players:
            card1 = random.choice(self.deck)
            player.cards.append(card1)
            self.deck.remove(card1)

            card2 = random.choice(self.deck)
            player.cards.append(card2)
            self.deck.remove(card2)


    def flop(self):
        self.card1 = random.choice(self.deck)
        self.board.append(self.card1)
        self.deck.remove(self.card1)

        self.card2 = random.choice(self.deck)
        self.board.append(self.card2)
        self.deck.remove(self.card2)

        self.card3 = random.choice(self.deck)
        self.board.append(self.card3)
        self.deck.remove(self.card3)

        print('dealer flops ' + self.card1 + ' ' + self.card2 + ' ' + self.card3)


    def turn(self):
        self.card4 = random.choice(self.deck)
        self.board.append(self.card4)
        self.deck.remove(self.card4)

        print('dealer turns ' + self.card4)


    def river(self):
        self.card5 = random.choice(self.deck)
        self.board.append(self.card5)
        self.deck.remove(self.card5)

        print('The river is ' + self.card5)


    def showdown(self):
        print('The Board is '  + self.card1 + ' ' + self.card2 + ' ' + self.card3 + ' ' + self.card4 + ' ' + self.card5)
        for player in self.active_players:
            print(player.name + ' is in with ' + player.cards[0] + player.cards[1])

    def checkhands(self, _player):
        pass


    def betround(self, start):
        self.active_players = [player for player in self.Players if  player.active]
        #first round
        for player in self.active_players:
            self.act(player)

        while True:

            self.active_players = [player for player in self.Players if  player.active]
            # Get the bet of the first player
            first_player_bet = self.active_players[0].bet

            # Check if all players have the same bet
            if all(player.bet == first_player_bet for player in self.active_players):
                break  # Exit the loop if all bets are the same

            # Iterate through players and update bets as needed
            for player in self.active_players:
                if player.bet is not self.toCall:
                    self.act(player)

        for player in self.Players:
            self.pot += player.bet
            player.bet = 0

        print('The currnet Pot is worth ' + str(self.pot))
        
    
    def calling(self, _player):
        _player.stack -= self.toCall - _player.bet
        _player.bet = self.toCall
        print(_player.name + ' calls ' + str(self.toCall))

    def folding(self, _player):
        _player.active = False
        print(_player.name + ' folds')

    def raising(self, _player):
        self.toCall = self.toCall * 2
        _player.stack -= self.toCall - _player.bet
        _player.bet = self.toCall
        print(_player.name + ' raises to ' + str(self.toCall))


    def act(self, _player):
        match _player.decide(self.pot, self.toCall): 
            case 'call':
                self.calling(_player)
            case 'fold':
                self.folding(_player)
            case 'raise':
                self.raising(_player)
