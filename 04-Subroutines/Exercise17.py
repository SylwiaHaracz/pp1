def different(a, b, c):
    if a!=b and b!=c and c!=a:
        return True
    else: 
        return False

n1= int(input('Enter 1st number: '))
n2= int(input('Enter 2nd number: '))
n3= int(input('Enter 3rd number: '))

if different(n1, n2, n3)==True:
    print('Trueeee')
else:
    print('False :(')