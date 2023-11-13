def f(number, even):
    number = str(number)
    sum = 0
    if even == True:
        for i in range (0, len(number)):
            if number[i] == '0' or number[i] == '2' or number[i] == '4' or number[i] == '6' or number[i] == '8':
                a= number[i]
                a=int(a)
                sum = sum +a
                i+=1
            else:
                continue

    else:
        for i in range (0, len(number)):
            if number[i] == '1' or number[i] == '3' or number[i] == '5' or number[i] == '7' or number[i] == '9':
                a= number[i]
                a=int(a)
                sum = sum +a
                i+=1
            else:
                continue
    return sum

if __name__=="__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))
