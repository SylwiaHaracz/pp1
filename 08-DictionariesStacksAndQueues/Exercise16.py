Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

sum_Krakow = 0
n=0
while n<len(Hotels_in_Krakow):
    price_krakow=Hotels_in_Krakow[n]
    sum_Krakow+=price_krakow["price"]
    n+=1

average_krakow = sum_Krakow/len(Hotels_in_Krakow)

sum_Sopot = 0
m=0
while m<len(hotels_in_Sopot):
    price_sopot=hotels_in_Sopot[m]
    sum_Sopot+=price_sopot["price"]
    m+=1

average_sopot = sum_Sopot/len(hotels_in_Sopot)


print(f'Average in Krakow: {average_krakow}')
print(f'Average in Sopot: {average_sopot}')

if average_krakow<average_sopot:
    print('Hotels in Kraków are cheaper')
else:
    print('Hotels in Sopot are cheaper')