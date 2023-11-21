def second_largest(arr):
    arr2 = list(set(arr))
    return arr2[-2]

def mediana(arr):
    arr2 = list(set(arr))
    return arr2[len(arr2)//2]

def smallest_and_largest(arr):
    arr2 = list(set(arr))
    arr3 = [arr2[0], arr2[-1]]
    return arr3

def minus(arr):
    result=""
    for i in arr:
        result=result+str(i)+'-'
    return result[:-1]
    

