arr1 = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

for i in range (len(arr1)):
    for j in range (len(arr1[0])):
        if i ==j:
            arr1[i][j]=1

print(arr1)