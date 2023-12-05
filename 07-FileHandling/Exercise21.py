file = open("numbers1-50","w")
for i in range (1,51):
    num=str(i) + "\n"
    file.write(num)

file.close()