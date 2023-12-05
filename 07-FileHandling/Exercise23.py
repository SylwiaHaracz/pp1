file=open("second_and_third_power.txt","w")
for i in range(1,11):
    first = str(i)
    second = str(i**2)
    third = str(i**3)
    result = first+", "+second+", "+third+"\n"
    file.write(result)

file.close()