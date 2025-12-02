import requests as rq

url = "https://swapi.dev/api/films"
response = rq.get(url).json()

print("REST Results:")

for i in response['results']:
    print(f"{i['title']} ({i['episode_id']}): {i["release_date"]}")