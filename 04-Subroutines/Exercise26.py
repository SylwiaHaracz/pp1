def even_or_odd(a):
    if a%2==0:
        return True
    else:
        return False
    
if __name__ =="__main__":
    x = int(input('Enter a number: '))
    print(f'Your number is even: {even_or_odd(x)}')