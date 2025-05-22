import json

with open("match_0.json","r",encoding="utf-8") as f:
    matches = json.load(f)

with open("timeline_0.json","r",encoding="utf-8") as f:
    timelines = json.load(f)

match = matches[0]['info']
timelines = timelines[0]['info']

first_player = match['participants'][0]
first_player_id = first_player['participantId']

print(f"Champion : {first_player['championName']}, pid {first_player_id}")

minutes = 14
to_extract = 'totalGold'
single_frame = timelines["frames"][minutes]
target_time = single_frame['timestamp'] / 60000
totalGold = single_frame['participantFrames'][str(first_player_id)]['totalGold']
print(f"{to_extract} at {target_time:.2f} minutes : {totalGold}")