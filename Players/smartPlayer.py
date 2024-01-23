import json
import tensorflow as tf
import numpy as np

class Player:
    def __init__(self, _name):
        self.name = _name
        self.cards = []
        self.stack = 1000
        self.bet = 0
        self.active = True

    def decide(self, _pot, _numPlayers, *_cards):
        data = []

        possibleDecisions = ['c', 'c', 'r', 'f', 'c']

        possibleCards = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                        '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                        '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                        '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]

        cardMetric = []

        cardMetric.append(0)
        cardMetric.append(4)
        cardMetric.append(_numPlayers)
        cardMetric.append(_pot)


        for card in possibleCards:
            if card in _cards:
                cardMetric.append(1)
            else:
                cardMetric.append(0)
        data.append(cardMetric)


        model = tf.keras.models.load_model('Models\\nn.h5')
        prediction = model.predict(data)
        print(possibleDecisions[np.argmax(prediction[0])])


with open("trainingData/hands_valid.json", "r") as read_file:
    data = json.load(read_file)
for game in data:
    if game['id'] > 1000:
        d = game['dealer']
        p_num = game['num_players']
        pots_p_num = game['pots'][1]['num_players']
        pot = game['pots'][1]['size']

        cards = game['players'][-1]['pocket_cards'] + [game['board'][0], game['board'][1], game['board'][2]]

        possibleCards = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                        '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                        '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                        '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]

        cardMetric = []

        cardMetric.append(d)
        cardMetric.append(p_num)
        cardMetric.append(pots_p_num)
        cardMetric.append(pot)

        for card in possibleCards:
            if card in cards:
                cardMetric.append(1)
            else:
                cardMetric.append(0)

p1 = Player('Tobi')
p1.decide(1000, 3, ['4d', 'Qh', '2c', '7h', 'Ts'])