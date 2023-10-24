name = input('Enter a name: ')
lenght = len(name)
if name[lenght-1]=='a':
    print(f'{name} is a Polish female name')
else:
    print(f'{name} is NOT a Polish female name')