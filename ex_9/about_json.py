import requests as rq
import json

url = "http://jonghyup.com/tmp/data.json"

req = rq.get(url).json()

for i in req["items"]:
    print(i)  # value
    print("===========================")

for i in req["items"]:
    if i["age"] >= 30:
        print(f"name: {i['name']}, age: {i['age']}, email: {i['email']}")

print("===========================")

for i in req["items"]:
    if i["private"]["weight"] >= 50:
        print(f"name: {i['name']}, age: {i['age']}, weight: {i['private']['weight']}")