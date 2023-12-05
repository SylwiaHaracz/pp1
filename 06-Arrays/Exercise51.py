arr=[[1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3]]

pom = arr[0]
print(arr)
for i in range (0, len(arr)):
    if i  == 0:
        arr[i]=arr[-1]
    elif i == len(arr)-1:
        arr[i] =pom
    else:
        arr[i]=arr[i]

print(arr)