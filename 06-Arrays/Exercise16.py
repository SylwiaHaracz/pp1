arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

suma = 0
for i in range (0, len(arr)):
    for j in arr[i]:
        if j%2==1:
            suma = suma+j

print(suma)