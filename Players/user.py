import tkinter as tk

class Player:
    def __init__(self, _name):  
        self.name = _name           #creating the Player
        self.cards = []
        self.stack = 1000
        self.bet = 0
        self.active = True

    def decide(self, stage, board):
        self.decision = ""
        self.choice=tk.Tk() #creating the main window and storing the window object in 'win'
        self.choice.geometry('300x80')
        call_btn = tk.Button(self.choice, text='call', command=self.call)
        raise_btn = tk.Button(self.choice, text='raise', command=self.raises)
        fold_btn = tk.Button(self.choice, text='fold', command=self.fold)
        call_btn.pack()
        raise_btn.pack()
        fold_btn.pack()
        self.choice.mainloop()
        return self.decision

    def call(self):
        self.decision = 'call'
        self.choice.quit()
        self.choice.destroy()
    def raises(self):
        self.decision = 'raise'
        self.choice.quit()
        self.choice.destroy()
    def fold(self):
        self.decision = 'fold'
        self.choice.quit()
        self.choice.destroy()