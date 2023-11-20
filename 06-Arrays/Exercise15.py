arr = [[1,3,5],[8,7,2]]
print(arr[0][0]+arr[-1][-1])
#print(arr[0][1]+arr[1][1])
#print(arr[1][0]+arr[1][1]+arr[1][2])

suma1=0
for i in range (0, len(arr)):
    suma1 = suma1 + arr[i][len(arr)//2]

print(suma1)


suma2=0
for j in arr[1]:
    suma2=suma2+j

print(suma2)