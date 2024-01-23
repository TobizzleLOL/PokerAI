from PokerGame import Game as PokerGame
from models import randomPlayer as rP


#creating the player objects
'''p1 = rP.Player('Stewie')
p2 = rP.Player('Brian')'''
p3 = rP.Player('Peter')
p4 = rP.Player('Lois')

#creating the game object
Game = PokerGame.Game(p3, p4, dealmode='manuel') #dealmode manuel/auto

#dealmode manuel takes cards for testing
'''p1.cards = ['2s', '4s']
p2.cards = ['2h', '4h']'''
p3.cards = ['5c', '5c']
p4.cards = ['2d', '3d']
Game.board = ['4d', '5d', '6d', '7d', '6c']

Game.start()