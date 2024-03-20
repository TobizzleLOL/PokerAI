import random
import PokerGame.hands as hands
import csv
deck = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                     '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                     '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                     '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]
datas = []

def convert(hand):
    rank = hands.determine_hand([' '.join(hand)])
    data = []
    card_value = dict(zip('A 2 3 4 5 6 7 8 9 T J Q K'.split(), range(13)))      #dictionary for cardvalues
    suit_value = dict(zip('c h s d'.split(), range(4)))                         #dictionary for suitvalues

    for card in hand:
        c, s = list(card) # Splits the cards for example c=9 ; s = h

        c = card_value[c]+1     #translating to values
        s = suit_value[s]+1 
        data.append(s)
        data.append(c)
    data.append(rank)
    return data     #appending all the elements for example data=[1, 3, 4, 2, 10, 2, 11, 1, 6, 4]

def create():
    hand = random.sample(deck, 5)
    datas.append(convert(hand))


for i in range(0, 100000):
    create()

with open('flop2_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(datas)
        print(datas)