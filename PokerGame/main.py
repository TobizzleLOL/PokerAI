from packages import PokerGame
from models import random as randomPlayer

p1 = randomPlayer.Player('Stewie')
p2 = randomPlayer.Player('Brian')
p3 = randomPlayer.Player('Peter')
p4 = randomPlayer.Player('Lois')


Game = PokerGame.Game(p1, p2, p3, p4)
Game.start()