time24h = input('Enter time in 24h format: ')

if len(time24h)==4:
    print(f'Time in 12-hour format: {time24h}am')
elif len(time24h)==5:
    hours = int(time24h[0:2])
    hours12h = hours - 12
    minutes = time24h[-2:]
    print(f'Time in 12-hour format: {hours12h}:{minutes}pm')
else:
    print('Enter time in 24h format (hh:mm)!')
