arr=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

pom=[]

for i in range (0, len(arr)):
    pom.append(arr[i][0])

for i in range (0, len(arr)):
    for j in range (0, len(arr[0])):
        if j==0:
            arr[i][j]=arr[i][-1]
        elif j ==len(arr[0])-1:
            arr[i][j]=pom[i]
        else:
            arr[i][j]=arr[i][j]


print(arr)