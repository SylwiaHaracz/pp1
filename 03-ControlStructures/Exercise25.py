number_of_products = int(input('Number of products purchased: '))
price = float(input('Product price: '))
if number_of_products>2:
    bill = 2*price + (number_of_products-2)*(price*0.75)
    print(f'Amount to pay: {bill}')
else: 
    bill2 = price*number_of_products
    print(f'Amount to pay: {bill2}')