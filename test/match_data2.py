import json

from urllib3 import proxy_from_url

with open("match_0.json", "r", encoding="utf-8") as f:
    data = json.load(f)

single_match = data[0]

metadata = single_match["metadata"]
info = single_match["info"]

print(metadata)
print(len(metadata['participants']))

import datetime
time = info["gameCreation"]
print(time)
time = time // 1000
d = datetime.datetime.fromtimestamp(time, datetime.UTC)
print(d)

print("*** LoL 매치데이터 정보 ***")
print(f"Match Id : {metadata["matchId"]}")
print(f"게임 생성 시간 : {d.strftime('%Y년 %m월 %d일 %H시 %M분')}")
print(f"게임 플레이 시간 : {info["gameDuration"]//60}분 {info["gameDuration"] % 60}초")
paticipants = info["participants"]
p = paticipants[0]
if p["win"]:
    winteam = "블루" if p["teamId"] == 100 else "레드"
else:
    winteam = "레드" if p["teamId"] == 100 else "블루"
print(f"승리 팀 : {winteam}")

print("\n** 플레이어 정보 **")
for p in paticipants:
    print(f"포지션 : {p["teamPosition"]}")
    print(f"팀 : {"블루" if p["teamId"] == 100 else "레드"}")
    print(f"챔피언 : {p["championName"]}")
    k = p["kills"]; d = p["deaths"]; a = p["assists"]
    kda = (k+a) / (1 if d == 0 else d)
    print(f"K/D/A : {k}/{d}/{a}, KDA : {kda:.1f}")
    print(f"챔피언에게 가한 데미지 : {p["totalDamageDealtToChampions"]}")
    print(f"받은 데미지 : {p["totalDamageTaken"]}")
    print(f"골드 획득량 : {p["goldEarned"]}")
    print(f"경험치 획득량 : {p["champExperience"]}")
    print()

print(len(data))
print(type(data))
print(type(metadata))
print(type(info))
