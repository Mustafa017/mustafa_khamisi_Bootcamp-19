import requests, pprint, json

url = 'http://api.football-data.org/v1/teams/66/'
r = requests.get(url)
result = json.loads(r.text)

pprint.pprint(result)
 