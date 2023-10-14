regestration_number = input('Enter your vehicle registration number\n')
city = regestration_number[0:2]
Krakow = city=='KR' or city=='KK'
print(f'Car from Kraków: {Krakow}')