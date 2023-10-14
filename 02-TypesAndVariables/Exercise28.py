height = float(input('Enter your height in cm\n'))
weight = float(input('Enter your weight in kg\n'))
height_in_meters = height/100
bmi = weight/(height_in_meters**2)
correct = bmi>=18.5 and bmi<=24.9
print(f'Your BMI: {bmi}')
print(f'Correct weight: {correct}')