person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(f'Content: {person}')
print(f'Name: {person["name"]}')
print(f'Hobby: {person["hobby"]}')
person["surname"]="Nowak"
person["married"]=not person["married"]
person["gender"]="Male"
person["hobby"].append("bicycle")
#person["hobby"]=person["hobby"]+["bicycle"]
person["phone"]["workphone"]='313131444'
print(f'New content: {person}')