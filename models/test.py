import json

with open("trainingData/hands_valid.json", "r") as read_file:
    data = json.load(read_file)

for game in data:
    print(game['players'][0]['bets'][1]['actions'][0])