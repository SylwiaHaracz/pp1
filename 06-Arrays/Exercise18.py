arr=[[True,False],[True,True],[False,False]]
print(f'Before: {arr}')

for i in range (0, len(arr)):
    for j in range (0,len(arr[0])):
        if arr[i][j] == True:
            arr[i][j] = False
        else:
            arr[i][j] = True

print(f'After:{arr}')