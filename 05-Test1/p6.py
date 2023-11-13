def f(number,even):
    number = str(number)
    result = 0
    if even == True:
        for i in number:
            if i == '0' or i=='2' or i =='4' or i =='6' or i=='8':
                result = result + int(i)
    if even == False:
        for i in number:
            if i == '1' or i=='3' or i =='5' or i =='7' or i=='9':
                result = result + int(i)
    return result

if __name__=="__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))