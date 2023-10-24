number1 = int(input('Enter 1st number: '))
number2 = int(input('Enter 2nd number: '))
if number1 >=0 or number2 >=0:
    print(f'At least one of the numbers ({number1} and {number2}) is not negative')
else:
    print(f'Both of the numbers ({number1} and {number2}) are negative')