import random
dice = random.randrange(1, 6, 1)
special = dice==1 or dice==6
print(f'Dice rolled: {dice}')
print(f'Special: {special}')