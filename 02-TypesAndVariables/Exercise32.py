price = float(input('Enter a price you paid\n'))
tax = price*0.23
tax_round = round(tax,2)
print(f'Your amount: {price}')
print(f'Tax: {tax_round}')