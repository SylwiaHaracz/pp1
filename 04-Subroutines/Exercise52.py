def power(x,n):
    if n>1:
        result = x*x**(n-1)
        return result
    elif n==1:
        return 1
    else:
        return "You're stupid!"

if __name__=="__main__":
    print(power(5,3))