from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

model = tf.keras.models.load_model('Models\\\model_flop_test8.keras')


test = pd.read_csv("trainingData\\flop_data.csv",
                    header=None,
                    names=["S1","C1","S2","C2","S3","C3","S4","C4","S5","C5","hand"])
test.sample(10)

test2 = test
pred = model.predict(test.drop("hand",axis=1).values).T
test2["high_card"] = pred[0]
test2["paerchen"] = pred[1]
test2["zwei_paerchen"] = pred[2]
test2["drillinge"] = pred[3]
test2["straight"] = pred[4]
test2["flush"] = pred[5]
test2["full_house"] = pred[6]
test2["vierlinge"] = pred[7]
test2["straight_flush"] = pred[8]
test2["royal_flush"] = pred[9]


group = test2.groupby("hand").agg({"high_card":["mean"],
                                   "paerchen":["mean"],
                                   "zwei_paerchen":["mean"],
                                   "drillinge":["mean"],
                                   "straight":["mean"],
                                   "flush":["mean"],
                                   "full_house":["mean"],
                                   "vierlinge":["mean"],
                                   "straight_flush":["mean"],
                                   "royal_flush":["mean"]})
group.index = ["high_card",
               "paerchen",
               "zwei_paerchen",
               "drillinge",
               "straight",
               "flush",
               "full_house",
               "vierlinge",
               "straight_flush",
               "royal_flush"]
group.columns = group.columns.get_level_values(0)
round(group,2)

sns.heatmap(round(group,2),annot=True)
plt.ylabel("Echte Hand")
plt.xlabel("Geschätzte Hand")
plt.show()