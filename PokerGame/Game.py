import random
from .packages import hands as ev

class Game():
    def __init__(self, *Players, dealmode):     
        self.Players = Players          #List with all the Players [p1,p2,p3,...]
        self.dealmode = dealmode        #Dealmode manuel/auto

        self.deck = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                     '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                     '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                     '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]
        self.board = []
        self.pot = 0
        self.blindsize = 2
        self.toCall = self.blindsize

    def start(self):
        if self.dealmode == 'manuel':   #skips all the card dealing
            self.blinds()
            self.betround(2)
            self.betround(0)
            self.betround(0)
            self.betround(0)
        else:                           #includes card dealing
            self.board = []             #clears board is case it got defined
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

    #takes blinds according to self.blindsize from first two Players
    def blinds(self):
        self.Players[0].bet = 0.5 * self.blindsize
        self.Players[1].bet = 1.0 * self.blindsize

    #deals random cards to every Player
    def deal(self):
        for player in self.Players:
            player.cards = []                   #clears every players cards in case they got defined
            card1 = random.choice(self.deck)
            player.cards.append(card1)
            self.deck.remove(card1)

            card2 = random.choice(self.deck)
            player.cards.append(card2)
            self.deck.remove(card2)

    #adds 3 community cards to the board
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

    #adds a 4th community card to the board
    def turn(self):
        self.card4 = random.choice(self.deck)
        self.board.append(self.card4)
        self.deck.remove(self.card4)

        print('dealer turns ' + self.card4)

    #adds a 5th community card to the board
    def river(self):
        self.card5 = random.choice(self.deck)
        self.board.append(self.card5)
        self.deck.remove(self.card5)

        print('The river is ' + self.card5)

    #evaluates every Players Hand and determines a Winner
    def showdown(self):
        max = 0
        winners = []
        print('The Board is '  + str(' '.join(self.board)))
        for player in self.active_players:
            print(player.name + ' is in with ' + player.cards[0] + player.cards[1])
            boardAndPlayer = [' '.join(self.board + player.cards)]
            handValue = ev.determine_hand(boardAndPlayer) # 1 = High Card, 2: Pair, 3: Two Pair, 4: Three of a Kinds 5: Straight, 6: Flush, 7: Full-House, 8: Four of a Kind, 9: Straight-Flush, 10: Royal Flush
            if handValue > max:
                max = handValue
                winners = []
                winners.append(player)
            elif handValue == max:
                winners.append(player)

            match handValue:
                case 10:
                    print(player.name + ' got a Royal Flush! ')
                case 9:
                    print(player.name + ' got a Straight-Flush! ')
                case 8:
                    print(player.name + ' got a Four of a Kind! ')
                case 7:
                    print(player.name + ' got a Full-House! ')
                case 6:
                    print(player.name + ' got a Flush! ')
                case 5:
                    print(player.name + ' got a Straight! ')
                case 4:
                    print(player.name + ' got Three of a Kind! ')
                case 3:
                    print(player.name + ' got a Two Pair! ')
                case 2:
                    print(player.name + ' got a Pair! ')
                case 1:
                    print(player.name + ' got High Card! ')

        for player in winners:
            print(player.name+ ' wins!')


            


    #cycles through every player until everyone either folds or calls
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
        
    
    #calling the current bet
    def calling(self, _player):
        _player.stack -= self.toCall - _player.bet
        _player.bet = self.toCall
        print(_player.name + ' calls ' + str(self.toCall))

    #folding the hand
    def folding(self, _player):
        _player.active = False
        print(_player.name + ' folds')

    #raising the pot            [WIP]raise amount
    def raising(self, _player):
        self.toCall = self.toCall * 2
        _player.stack -= self.toCall - _player.bet
        _player.bet = self.toCall
        print(_player.name + ' raises to ' + str(self.toCall))

    #queries a players decision
    def act(self, _player):
        match _player.decide(self.pot, self.toCall): 
            case 'call':
                self.calling(_player)
            case 'fold':
                self.folding(_player)
            case 'raise':
                self.raising(_player)
