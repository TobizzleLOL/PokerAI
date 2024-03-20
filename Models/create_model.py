import pandas as pd
import tensorflow as tf
from keras.utils import to_categorical


train_data = pd.read_csv('trainingData\\flop_data.csv',
                    header=None,
                    names=["suite1","value1","suite2","value2","suite3","value3","suite4","value4","suite5","value5","hand"])
train_data.sample(10)

test_data = pd.read_csv('trainingData\\flop_data.csv',
                    header=None,
                    names=["suite1","value1","suite2","value2","suite3","value3","suite4","value4","suite5","value5","hand"])
test_data.sample(10)

train_data.hand.value_counts(normalize=True)


X = train_data.drop("hand",axis=1).values
y = train_data.hand.values
print(y)

dummy_y = to_categorical(y)
print(X.shape)


model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(52, input_dim=X.shape[1], kernel_initializer='normal', activation='relu'),
    tf.keras.layers.Dense(1000, kernel_initializer='normal', activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
    ])

model.compile(
    loss='categorical_crossentropy', 
    optimizer='adam', 
    metrics=['accuracy']
    )

model.fit(X, dummy_y, epochs=50, batch_size=25)

model.save('model_flop_test2.keras')

