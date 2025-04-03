import json
with open("master_page_player_info.json", 'r',encoding='utf-8') as f:
    data= json.load(f)

print(type(data))
print(data[0])
print(data[0]['puuid'])

master_puuids = []

for j,player in enumerate(data):
    print(j+1,player)
    print('puuid: ',player['puuid'])
    print('puuid: ', data[j]['puuid'])
    master_puuids.append(player['puuid'])
    print('----')

print(master_puuids)