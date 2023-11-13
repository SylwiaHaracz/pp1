def f(amount_to_pay):
    piec=0
    dwa=0
    jeden=0
    while amount_to_pay>=5:
        amount_to_pay -=5
        piec+=1
    while amount_to_pay>=2:
        amount_to_pay -=2
        dwa+=1
    while amount_to_pay>=1:
        amount_to_pay-=1
        jeden+=1
    monety = piec+dwa+jeden
    return monety
    
if __name__=="__main__":
    print(f'23- {f(23)}')
    print(f'8 - {f(8)}')
    print(f'0 - {f(0)}')