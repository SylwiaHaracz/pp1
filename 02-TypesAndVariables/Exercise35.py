circumference = float(input('Enter circumference of the tree in cm\n'))
diameter = circumference*2
to_cut = diameter >= 50
print(f'The tree is ready to be cut down: {to_cut}')