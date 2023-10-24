original_pin = '0805'
for i in range(3):
    pin = input('Enter your PIN number: ')
    if pin == original_pin:
        print('Correct!')
        break
    else:
        print('Incorrect PIN number')