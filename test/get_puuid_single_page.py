from http.client import responses
from wsgiref.headers import Headers

import requests
import json

#https://kr.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/MASTER/I?page=49&api_key=RGAPI-28fc5371-3acc-4ed4-93e0-0011ec00ef85

API_KEY = "RGAPI-28fc5371-3acc-4ed4-93e0-0011ec00ef85"
Headers = {"X-Riot-Token" : API_KEY}

QUEUE = "RANKED_SOLO_5x5"
TIERS = ["MASTER","GRANDMASTER","CHALLENGER"]
REGION = "kr"

def get_puuid_from_tier(queue,tier,region,divison="I"):
    url= f"https://{REGION}.api.riotgames.com/lol/league-exp/v4/entries/{queue}/{tier}/{divison}?page=1"
    print(url)
    response = requests.get(url, headers=Headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"ERROR: {response.status_code}")

# Master의 1페이지에 대한 puuid가 담긴 RESPINSE BODY를 읽어들인다.
# data_master = get_puuid_from_tier(QUEUE,TIERS[0],REGION)
# with open("master_player_info_from_python.json",'w',encoding='utf-8') as f:
#   json.dump(data_master, f, ensure_ascii=False, indent=4)

def get_puuid_from_tier_with_pages(queue, tier, region, divison='I'):
    page = 1
    all_data = []
    while True:
        url= f"https://{REGION}.api.riotgames.com/lol/league-exp/v4/entries/{queue}/{tier}/{divison}?page={page}"
        print(url)
        response = requests.get(url, headers=Headers)
        
        if response.status_code == 200:
            all_data.extend(response.json())
        else:
            raise Exception(f"ERROR: {response.status_code}")
        
        if not response.json():
            break
        
        page += 1
    return all_data
data = get_puuid_from_tier_with_pages(QUEUE, TIERS[0], REGION)
with open(f"puuid{TIERS[0]}_list.json","w",encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)