import pandas as pd
import tensorflow as tf
import numpy as np

class Player:
    def __init__(self, _name):
        self.name = _name
        self.cards = []
        self.stack = 1000
        self.bet = 0
        self.active = True

    def decide(self, _cards, _stage):
        data = []

        card_value = dict(zip('A 2 3 4 5 6 7 8 9 T J Q K'.split(), range(13)))
        suit_value = dict(zip('c h s d'.split(), range(4)))

        for card in _cards:
            c, s = list(card) # Splits the cards
            
            c = card_value[c]+1 #Converted Cards to value e.g [0, 1, 2, 3, 12]
            s = suit_value[s]+1
            data.append(s)
            data.append(c)
        print(data)

        model = tf.keras.models.load_model('Models\model.keras')
        prediction = model.predict([data])
        hand_value = np.argmax(prediction)
        if _stage == 'flop':
            match hand_value:
                case 0:
                    return 'fold'
                case 1:
                    return 'call'
                case 1:
                    return 'call'
                case _:
                    return 'raise'
            

p1 = Player('Tobi')
print(p1.decide(['Qh', '4d', 'Td', '3s', 'Kc'], 'flop'))