import json

with open("match_0.json","r",encoding="utf-8") as f:
    data = json.load(f)

correct_pred = 0
to_extract = 'goldEarned'
for j,match in enumerate(data):
    total_red, total_blue = 0,0
    info = match['info']
    players= info['participants']


    for p in players:
        damage = p['totalDamageDealtToChampions']
        if p['teamId'] == 100:
            total_blue+= damage
        else:
            total_red += damage
    winner = ""
    if players[0]['win']:
        winner = "블루" if players[0]['teamId'] == 100 else "레드"
    else:
        winner = "레드" if players[0]['teamId'] == 100 else "블루"


    pred_winner = "블루" if total_blue > total_red else "레드"

    if winner == pred_winner: correct_pred += 1



    print(f"{j+1:2d}번째 매치 : 승리팀 - {winner},예측 - {pred_winner}")
    print(f"{to_extract} : 레드팀 - {total_red}, 블루팀 - {total_blue}\n")
    print(f"승리팀 : {winner}\n")
    # print(f"{j+1:2d}-th match id: {match["metadata"]["matchId"]}")

print(f"{to_extract} 변수의 예측 정확도 : {correct_pred/len(data):.2f}")