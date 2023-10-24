name1 = input('Enter the name of 1st person: ')
age1 = int(input('Enter the age of 1st person: '))
name2 = input('Enter the name of 2nd person: ')
age2 = int(input('Enter the age of 2nd person: '))
if age1>=18 and age2>=18:
    print(f'Both {name1} and {name2} are adults')
else:
    print(f'At least one ofthem is underage')