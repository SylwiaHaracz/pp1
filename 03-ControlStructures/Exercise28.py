EAN13 = input('Enter EAN-13 article number: ')
if len(EAN13)==13:
    print('Article number is correct')
    if EAN13[0] == '5' and EAN13[1] == '9' and EAN13[2] == '0':
        print('Article manufactured in Poland')
else:
    print('Article number is not correct')