def f(card_number):
    first = card_number[0:2]
    last = card_number[12:]
    return first+"**********"+last

if __name__=="__main__":
    print(f("5290312400019022"))