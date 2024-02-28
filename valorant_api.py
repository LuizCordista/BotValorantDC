import requests

def eloluoz():
  response = requests.get("https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/br/31d656bc-f37f-593e-b6e6-cd77bec0e4c5")
  return (response.json()["data"]["currenttierpatched"],
          response.json()["data"]["ranking_in_tier"],
          response.json()["data"]["images"]["small"])


def elorandom(name, tag):
  puuid = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}").json()["data"]["puuid"]
  response = requests.get(f"https://api.henrikdev.xyz/valorant/v1/by-puuid/mmr/br/{puuid}")
  return (response.json()["data"]["currenttierpatched"],
          response.json()["data"]["ranking_in_tier"],
          response.json()["data"]["images"]["small"])

print(eloluoz())
  


