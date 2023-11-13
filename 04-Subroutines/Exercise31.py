def f(x,y):
    num = 0
    for i in range (x,0):
        if i%2==0:
            num=num + 1
    return num

if __name__=="__main__":
    print (f(-7,8))
    print (f(-1,11))