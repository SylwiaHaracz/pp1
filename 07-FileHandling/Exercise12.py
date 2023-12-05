name = "Jan Kowalski"
uni = "Krakow University of Economics"
field = "Applied Informatics"

file = open("student.txt","w")

file.write(name+'\n')
file.write(uni+'\n')
file.write(field+'\n')

file.close()