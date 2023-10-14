buying_rate = float(input('Enter buying rate\n'))
selling_rate = float(input('Enter selling rate\n'))
spread = selling_rate - buying_rate
spread_rounded = round(spread,4)
print(f'Spread: {spread_rounded}')