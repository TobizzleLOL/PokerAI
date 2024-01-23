import json
import tensorflow as tf
import numpy as np

with open("trainingData/hands_valid.json", "r") as read_file:
    data = json.load(read_file)

train = []
train_lable = []
test = []
test_lable = []


#train data
for game in data:
  if game['pots'][1]['num_players'] > 0:
    if game['id'] < 1000:
      cards = game['players'][-1]['pocket_cards'] + [game['board'][0], game['board'][1], game['board'][2]]

      possibleCards = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                      '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                      '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                      '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]

      cardMetric = []

      for card in possibleCards:
          if card in cards:
            cardMetric.append(1)
          else:
            cardMetric.append(0)

      train.append(cardMetric)
      match game['players'][-1]['bets'][1]['actions'][-1]:
        case 'b':
          train_lable.append(0)
        case 'c':
          train_lable.append(1)
        case 'r':
          train_lable.append(2)
        case 'f':
          train_lable.append(3)
        case 'k':
          train_lable.append(4)

  #testdata
    elif game['id'] > 1000:
      cards = game['players'][-1]['pocket_cards'] + [game['board'][0], game['board'][1], game['board'][2]]

      possibleCards = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As',
                      '2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
                      '2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',
                      '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac',]

      cardMetric = []

      for card in possibleCards:
          if card in cards:
            cardMetric.append(1)
          else:
            cardMetric.append(0)


      test.append(cardMetric)

      match game['players'][-1]['bets'][1]['actions'][-1]:
        case 'b':
          test_lable.append(0)
        case 'c':
          test_lable.append(1)
        case 'r':
          test_lable.append(2)
        case 'f':
          test_lable.append(3)
        case 'k':
          test_lable.append(4)


model = tf.keras.models.Sequential([
      tf.keras.layers.Dense(52),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dense(128, activation='relu'),
      tf.keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train, train_lable, epochs=15)
model.evaluate(test, test_lable)
