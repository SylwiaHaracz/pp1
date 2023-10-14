height = float(input("What's your height?\n"))
foot = height*0.0328
foot_int = int(foot)
foot_left = foot - foot_int
inches = foot_left*12
print(f'Your height is {foot_int} feet and {inches} inches.')