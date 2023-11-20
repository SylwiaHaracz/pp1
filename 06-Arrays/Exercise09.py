arr = [2, 3, 7, 5, 4]

print(f'Array: {arr}')
print(f'Number of elements: {len(arr)}')
print(f'First value: {arr[0]}')
print(f'Second value: {arr[1]}')
print(f'Last but one: {arr[len(arr)-2]}')
print(f'Sum of first and last value: {arr[0]+arr[-1]}')
print(f'Middle value: {arr[len(arr)//2]}')

for i in arr:
    print(i,end=" ")


