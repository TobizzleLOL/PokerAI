from PokerGame import Game as PokerGame
from Players import randomPlayer as rP
from Players import smartPlayer as sP
from Players import user
import tensorflow as tf

tf.keras.utils.disable_interactive_logging()

#creating the player objects
p1 = sP.Player('Stewie')
p2 = sP.Player('Brian')
p3 = sP.Player('Peter')
p4 = sP.Player('Lois')
p5 = user.Player('Tobi')        #this is the user!


#creating the game object
Game = PokerGame.Game(p1, p2, p3, p4, p5, dealmode='manuel') #dealmode manuel/auto

#dealmode manuel takes cards for testing
p1.cards = ['4s', '4c']
p2.cards = ['6s', '7s']
p3.cards = ['8s', '9s']
p4.cards = ['2d', '3d']
p5.cards = ['Qc', 'Kh']
Game.board = ['4s', '2h', 'As']     #sadly only 3 cards because theres no model for turn scenario 

Game.start()