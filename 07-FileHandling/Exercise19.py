file = open("data.txt", "r", encoding='utf-8')
new = open("copylines.txt", "w", encoding='utf-8')
for line in file:
    new.write(line)

file.close()