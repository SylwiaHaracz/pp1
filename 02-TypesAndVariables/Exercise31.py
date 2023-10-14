import random
computer_dice = random.randrange(1,6,1)
user_dice = int(input('Guess the number '))
print (f'Computer dice: {computer_dice}')
right = computer_dice == user_dice
print(f'Your guess was: {right}')