def f(card_number):
    first2 = card_number[0:2]
    last2 = card_number[14:]
    return first2+"************"+last2



if __name__=="__main__":
    card= "5290312400019022"
    print(f(card))