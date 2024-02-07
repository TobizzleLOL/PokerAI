import pandas as pd
import tensorflow as tf
import numpy as np

class Player:
    def __init__(self, _name):
        self.name = _name           #creating the Player
        self.cards = []
        self.stack = 1000
        self.bet = 0
        self.active = True

    def decide(self, _stage, _board):           #this method is called when the game asks the player what it will do // 'raise', 'fold', 'call'
        self.allCards = _board + self.cards

        data = []

        card_value = dict(zip('A 2 3 4 5 6 7 8 9 T J Q K'.split(), range(13)))      #dictionary for cardvalues
        suit_value = dict(zip('c h s d'.split(), range(4)))                         #dictionary for suitvalues

        for card in self.allCards:
            c, s = list(card) # Splits the cards for example c=9 ; s = h
            
            c = card_value[c]+1     #translating to values
            s = suit_value[s]+1 
            data.append(s)
            data.append(c)      #appending all the elements for example data=[1, 3, 4, 2, 10, 2, 11, 1, 6, 4]
        
        if _stage == 'flop':
            model = tf.keras.models.load_model('Models\model_flop.keras')   #loading the model
            prediction = model.predict([data])                              #evaluating position via AI model                     
            hand_value = np.argmax(prediction)
            match hand_value:
                case 0:
                    return 'fold'
                case 1:
                    return 'call'
                case _:
                    return 'raise'
                
        if _stage == 'turn':
            model = tf.keras.models.load_model('Models\model_flop.keras') #still WIP there is no model for turn scenarions yet
            prediction = model.predict([data])
            hand_value = np.argmax(prediction)
            match hand_value:
                case 0:
                    return 'fold'
                case 1:
                    return 'call'
                case _:
                    return 'raise'