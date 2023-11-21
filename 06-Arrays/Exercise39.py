arr = [1,4,2,8,4,5,3,9,2]
arr_even=[]
arr_odd=[]
result=[]

for i in arr:
    if i%2==0:
        arr_even.append(i)
    else:
        arr_odd.append(i)

n=0
while n<len(arr_even):
    result.append(arr_even[n])
    n+=1
n=0
while n<len(arr_odd):
    result.append(arr_odd[n])
    n+=1

print(result)
