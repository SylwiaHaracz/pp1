file_name = input("Enter a file name: ")

file =  open(file_name, "r")
count = 0
for line in file:
    count+=1
file.close()

print(count)