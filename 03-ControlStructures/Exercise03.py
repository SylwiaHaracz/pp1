number = input('Enter a score\n')
try:
    number = float(number)
    if number<=1.0:
        if number >= 0.9:
            print("You're grade: A")
        elif number>=0.8:
            print("You're grade: B")
        elif number>=0.7:
            print("You're grade: C")
        elif number>=0.6:
            print("You're grade: D")
        elif number<0.6:
            print("You're grade: F")
    else:
        print('Write a correct number')

except:
    print('Write a number')