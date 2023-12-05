file = open("numbers.txt", "r")
suma = 0
for line in file:
    suma = suma  + int(line)
print(suma)
file.close()