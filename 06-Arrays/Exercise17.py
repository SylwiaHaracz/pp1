arr = [[0,0,0],[0,0,0],[0,0,0]]

for i in range (0, len(arr)):
    for j in range (0,len(arr[0])):
        if j==i:
            arr[i][j]=1

for row in arr:
    print(row)
