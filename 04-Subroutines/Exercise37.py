def f(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        fib_1=0
        fib_2=1
        for i in range (3, n+1):
            pom = fib_1
            fib_1 = fib_2
            fib_2 = pom + fib_2
        return fib_2
    

if __name__=="__main__":
    print(f(9))