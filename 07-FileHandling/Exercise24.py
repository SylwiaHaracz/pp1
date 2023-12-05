import csv
file = open("studentslist.csv", newline="")
csvreader = csv.reader(file)
rows = []
for row in csvreader:
    rows.append(row)

for i in range (1, len(rows)):
    if int(rows[i][2])<30:
        print(rows[i][0]," ", rows[i][1], " ", rows[i][-1])

file.close()