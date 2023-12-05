import json
movie = {
    "title":"Top Gun: Maverick",
    "year": 2022,
    "actor":{"leading":"Tom Cruise","supporting":"Myles Teller"},
    "oscar":False,
    "gerere": "Action"
}

with open("favourite.json", "w") as file:
    json.dump(movie, file, indent=5)