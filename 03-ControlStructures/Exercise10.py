number = float(input('Enter a number: '))
if number>=0:
    print(f'Wartość bezwzględna z liczby {number} wynosi {number}')
else:
    flipped = number*(-1)
    print(f'Wartość bezwzględna z liczby {number} wynosi {flipped}')