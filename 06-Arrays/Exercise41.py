def f(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return False
    return True

arr2 = [1,2,3]
arr1 = [5,4,3,1,2]

print(f(arr1,arr2))