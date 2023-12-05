import json

with open("data.json", "r") as file:
    data = json.load(file)



n=0
while n<len(data):
    row=data[n]
    for key,value in row.items():
        print(f'{key} : {value}')
    n+=1