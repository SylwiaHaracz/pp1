def check(a, x, y):
    if a>=x and a<=y:
        return True
    else:
        return False
    
if __name__=="__main__":
    a = int(input('Enter a number: '))
    x = int(input('Enter lowest point of przedział:'))
    y = int(input('Enter highest point of przedział: '))
    print(check(a, x, y))