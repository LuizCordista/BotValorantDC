import requests

def elovalorant(name, tag):
  puuid = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}").json()["data"]["puuid"]
  response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/br/{puuid}")
  return (response.json()["data"]["currenttierpatched"],
          response.json()["data"]["ranking_in_tier"],
          response.json()["data"]["images"]["small"])


  


