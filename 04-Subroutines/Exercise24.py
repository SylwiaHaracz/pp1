import in_range
number = int(input('Enter a number: '))
x = int(input('Enter lowest point of przedział:'))
y = int(input('Enter highest point of przedział: '))
print(f'Number {number} is in range <{x},{y}>: {in_range.check(number,x,y)}')