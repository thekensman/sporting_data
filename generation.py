import names
import math
import random
import uuid
import json

positions = ["Catcher", "Pitcher", "Runner", "Jumper", "Hitter"]
teams = ["Bearcats", "Pelicans", "Stars", "Stripes", "Eagles", "Bears"]

sporttastic_output = {}
superplayer_output = []

for team in teams:
  sporttastic_output[team] = []
  for i in range(30):
    position = positions[random.randrange(len(positions))]
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    id = str(uuid.uuid4())
    sporttastic_output[team].append({
        "id": id,
        "full_name": " ".join([first_name, last_name]),
        "team": team,
        "position": position,
        "weight": random.randrange(100, 300),
        "height": random.randrange(60, 78),
        "jersey": random.randrange(100),
        "start_year": random.randrange(2016, 2021),
        "current_year": 2021,
    })
    superplayer_output.append({
        "ID": id,
        "FirstName": first_name,
        "LastName": last_name,
        "CatchTotal": random.randrange(100) if position == "Catcher" else 0,
        "HitTotal": random.randrange(100) if position == "Hitter" else 0,
        "PitchTotal": random.randrange(100) if position == "Pitcher" else 0,
        "RunTotal": random.randrange(100) if position == "Runner" else 0,
        "JumpTotal": random.randrange(100) if position == "JumpTotal" else 0,
        "Team": team,
    })

print(json.dumps(sporttastic_output))
print("-------")
print(json.dumps(superplayer_output))
