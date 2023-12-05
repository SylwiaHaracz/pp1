arr = [[-38, 19], [5,40],[-7,11],[29,16]]
smallest_index = []
largest_index = []
min = arr[0][0]
max = arr[0][0]

for i in range (len(arr)):
    for j in range (len(arr[0])):
        current = arr[i][j]
        if current<=min:
            min = arr[i][j]
            smallest_index.append([i,j])

for i in range (len(arr)):
    for j in range (len(arr[0])):
        current = arr[i][j]
        if current>=max:
            max = arr[i][j]
            largest_index.append([i,j])


print(min, "  ", smallest_index[-1])
print(max, "  ", largest_index[-1])