binary = input('Enter 4-digit number in binary\n')
first = binary[0]
first = int(first)
second = binary[1]
second = int(second)
third = binary[2]
third = int(third)
fourth = binary[3]
fourth = int(fourth)
decimal = first*(2**3) + second*(2**2) + third*2 + fourth
print(f'Your number in decimal: {decimal}')