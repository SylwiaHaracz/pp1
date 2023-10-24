speed = float(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if speed<speed_limit_min or speed>speed_limit_max:
    print('Warning: invalid car speed!')
else:
    print("You're a great driver!")