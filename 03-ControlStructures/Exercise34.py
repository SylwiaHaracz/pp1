money = int(input('Enter your amount in PLN: '))
five = 0
two = 0
one = 0
while money>=5:
    money=money-5
    five= five+1
while money>=2:
    money=money-2
    two=two+1
while money>=1:
    money=money-1
    one=one+1

print (f'5zł : {five}')
print(f'2zł: {two}')
print(f'1zł: {one}')