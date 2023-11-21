def greater(arr, num):
    count = 0
    for i in arr:
        if i == num:
            count+=1
    return count

if __name__=="__main__":
    array = [1,2,5,2,9,3,5,6,8]
    number = int(input('Enter a number: '))
    print(greater(array, number))