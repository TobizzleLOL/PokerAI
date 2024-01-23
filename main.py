from PokerGame import Game as PokerGame
from models import randomPlayer as rP


#creating the player objects
p1 = rP.Player('Stewie')
p2 = rP.Player('Brian')
p3 = rP.Player('Peter')
p4 = rP.Player('Lois')

#creating the game object
Game = PokerGame.Game(p1, p2, p3, p4, dealmode='auto') #dealmode manuel/auto

#dealmode manuel takes cards for testing
p1.cards = ['2s', '3s']
p2.cards = ['2h', '3h']
p3.cards = ['2c', '3c']
p4.cards = ['2d', '3d']
Game.board = ['4c', '5h', 'Ac', 'Td', 'Kh']

Game.start()