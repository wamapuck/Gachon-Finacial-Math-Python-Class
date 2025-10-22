import random

flavor = {
    "Vanilla": 0,
    "Chocolate": 0,
    "Strawberry": 0,
    "Mint": 0,
    "Cookie Dough": 0
}

amount = 120

for i in range(amount):
    flavor_key = random.choice(list(flavor.keys()))
    if flavor_key == "Vanilla":
        flavor["Vanilla"] += 1
    elif flavor_key == "Chocolate":
        flavor["Chocolate"] += 1
    elif flavor_key == "Strawberry":
        flavor["Strawberry"] += 1
    elif flavor_key == "Mint":
        flavor["Mint"] += 1
    elif flavor_key == "Cookie Dough":
        flavor["Cookie Dough"] += 1

max_flavor = max(flavor, key=flavor.get)
print("Total Flavor Count: ", amount)
print("Flavors: ", flavor)
print("Top Flavor: ", max_flavor)