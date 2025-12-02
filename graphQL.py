import requests as rq

url = "https://swapi-graphql.netlify.app/.netlify/functions/index"

qer = """
{
  allFilms {
    films {
      title
      episodeID
      releaseDate
    }
  }
}
"""

res = rq.get(url, params={'query': qer}).json()

print("GraphQL Results:")

for i in res['data']['allFilms']['films']:
    print(f"{i['title']} ({i['episodeID']}): {i['releaseDate']}")