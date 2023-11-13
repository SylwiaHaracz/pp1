def f(amount_to_pay):
    piec=0
    dwa=0
    jeden=0
    suma=0
    while amount_to_pay>=5:
        amount_to_pay=amount_to_pay-5
        piec+=1
    while amount_to_pay>=2:
        amount_to_pay=amount_to_pay-2
        dwa+=1
    while amount_to_pay>=1:
        amount_to_pay=amount_to_pay-1
        jeden+=1
    suma = jeden + dwa + piec
    return suma

if __name__=="__main__":
    print(f(23))