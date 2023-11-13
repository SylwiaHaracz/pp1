def f(n):
    if n==1:
        return "*"
    elif n>1:
        gwiazdki = '*'
        for n in range (2,n+1):
            gwiazdki = gwiazdki + ("/*")
    return gwiazdki
    
if __name__=="__main__":
    print(f(1))
    print(f(4))