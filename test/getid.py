import json

with open("puuid_over_MASTER_tier.json", 'r' , encoding='utf-8') as f:
    data = json.load(f)

print("CHAALENGER의 첫번째 puuid")
print(data[0]["CHALLENGER"][0])
