def f(number1,number2,number3):
    maksymalny = max(number1, number2, number3)
    minimalny = min(number1, number2, number3)
    difference = maksymalny-minimalny
    return difference

if __name__=="__main__":
    print (f(7,4,9))
    print(f(2,12,8))