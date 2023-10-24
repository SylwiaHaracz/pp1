current_price = 140.00
previous_price = 200
discount = ((previous_price - current_price)*100)/previous_price
if discount>=10:
    print("Buy the product!!")
    print(f'Product price reduced by {discount}%')