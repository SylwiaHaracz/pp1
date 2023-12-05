import random
file = open("random_number.txt","w")
for i in range(0, 50):
    a= str(random.randint(100,999))+"\n"
    file.write(a)

file.close()