import json

with open("students.json", "r") as file:
    data = json.load(file)

n=0
data2=[]
while n<len(data):
    row=data[n]
    for key,value in row.items():
        if key =="name" or key == "surname" or key =="student_id":
            data2.append({key: value})
    n+=1

with open("limited.json", "w") as new:
    json.dump(data2, new, indent=5)