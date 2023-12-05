import re
file = open("grades.txt","r")
file_content = file.read()
grades = re.findall("\d+\.\d+", file_content)
sum = 0
for i in grades:
    sum+=float(i)
print(sum/len(grades))

file.close()