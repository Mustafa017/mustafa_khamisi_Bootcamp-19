import requests
import json

url = 'http://api.football-data.org/v1/teams/66/'
r = requests.get(url)
result = json.loads(r.text)

print (result)

	