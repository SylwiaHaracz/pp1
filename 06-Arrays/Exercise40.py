import random

arr=[]

for i in range (0, 8):
    arr.append(random.randint(0,999))

for i in range(0, 41):
    print("-", end="")
print()

for element in arr:
    print("|", end="")
    if element<10:
        print(f"   {element}", end="")
    elif element<100:
        print(f"  {element}", end="")
    elif element<1000:
        print(f" {element}", end="")
print("|")
for i in range(0, 41):
    print("-", end="")