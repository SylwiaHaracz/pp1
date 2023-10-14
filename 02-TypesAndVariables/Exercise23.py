a = float(input('Enter first side\n'))
b = float(input('Enter second side\n'))
c = float(input('Enter third side\n'))
p= (a+b+c)/2
area = (p*(p-a)*(p-b)*(p-c))**(0.5)
circumference = a+b+c
print(f'Arrea of your triangle: {area} and circumference: {circumference}')