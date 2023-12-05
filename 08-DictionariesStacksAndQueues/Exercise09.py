countries=[
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 1234567},
    {"name": "France", "population": 9876543},
    {"name": "Japan", "population": 438932},
    {"name": "Brasil", "population": 473256179}, 
]

n=0
print("Country\tPopulation")
while n<len(countries):
    country=countries[n]
    print(f'{country["name"]}\t{country["population"]}')
    n+=1