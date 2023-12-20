s = float(input('Enter distance in km: '))
h = float(input('Enter number of travel hours: '))
min = float(input('Enter number of travel minutes: '))

t= h+min/60

converter = lambda distance,time : distance/time
result = converter(s, t)
print(result)