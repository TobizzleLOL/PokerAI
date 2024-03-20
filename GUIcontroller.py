from tkinter import *
from PokerGame import Game as pg
from Players import randomPlayer as rP
from Players import smartPlayer as sP
from Players import user

class GUIcontroller():
    def __init__(self):
        window=Tk() #creating the main window and storing the window object in 'win'
        window.geometry('300x150')

        menu = Menu(window) 
        window.config(menu=menu) 

        game_menu = Menu(menu) 
        menu.add_cascade(label='Game', menu=game_menu) 

        game_menu.add_command(label='start game', command=self.start_Game) 
        game_menu.add_command(label='config', command=self.start_Game) 
        game_menu.add_command(label='select model', command=self.start_Game) 
        game_menu.add_command(label='run auto', command=self.start_Game) 

        window.mainloop() #running the loop that works as a trigger

    def start_Game(self):

        #creating the player objects
        p1 = sP.Player('Stewie')
        p2 = sP.Player('Brian')
        p3 = sP.Player('Peter')
        p4 = sP.Player('Lois')
        p5 = user.Player('Tobi')       #this is the user!

        #creating the game object
        self.Game = pg.Game(p1, p2, p3, p4, p5, dealmode='auto') #dealmode manuel/auto

        #dealmode manuel takes cards for testing
        p1.cards = ['4s', '4c']
        p2.cards = ['6s', '7s']
        p3.cards = ['8s', '9s']
        p4.cards = ['2d', '3d']
        p5.cards = ['Qc', 'Kh']
        self.Game.board = ['4s', '2h', 'As']     #sadly only 3 cards because theres no model for turn scenario 

        self.Game.board = []
        self.Game.deal()
        self.Game.flop()

        game_window=Tk() #creating the main window and storing the window object in 'win'
        game_window.title('Game')
        game_window.geometry('700x500')


        update_button = Button(game_window, text='next', command=self.next_round)
        update_button.pack()

        self.Game.blinds()
        
        for player in self.Game.Players:
            self.name = Label(game_window, text=player.name + "    " + player.cards[0] + player.cards[1], font=('Ariel', 20))
            self.name.pack()

        self.board = Label(game_window, text=self.Game.board[0]+self.Game.board[1]+self.Game.board[2], font=('Ariel', 20))
        self.board.pack()

        self.bets = []
        for i in range(len(self.Game.Players)):
            self.bet = Label(game_window, text=self.Game.Players[i].bet, font=('Ariel', 20))
            self.bets.append(self.bet)  
        
        for bet in self.bets:
            bet.pack()

        self.pot = Label(game_window, text=self.Game.pot, font=('Ariel', 30))
        self.pot.pack()


        game_window.mainloop() #running the loop that works as a trigger


    def next_round(self):
        self.Game.betround(0)
        for i in range(len(self.Game.Players)):
            self.bets[i].configure(text=self.Game.Players[i].bet)
        self.pot.configure(text=self.Game.pot)

gui = GUIcontroller()