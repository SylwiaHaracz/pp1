decimal = input('Enter a decimal number: ')
quotient = int(decimal)
reminders = ""
while quotient>0:
    reminders = str(quotient%2) + reminders
    quotient = quotient//2

print(f'{decimal}(10) = {reminders}(2)') 