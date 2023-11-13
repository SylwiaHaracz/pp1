def suma(n):
    if n>1:
        sum = n + suma(n-1)
        return sum
    elif n==1:
        return 1
    else:
        return "Your're stupid!"
    
    

if __name__=="__main__":
    print(suma(10))