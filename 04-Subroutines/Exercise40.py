def f(number):
    zero = 0
    jeden = 0
    dwa = 0
    trzy = 0
    cztery = 0
    piec = 0
    szesc = 0
    siedem = 0 
    osiem = 0
    dziewiec =0
    suma =0
    number = str(number)
    for i in range (0,len(number)):
        if number[i]=='0':
            zero = zero +1
        elif number[i]=='1':
            jeden = jeden +1
        elif number[i]=='2':
            dwa = dwa +1
        elif number[i]=='3':
            trzy = trzy+1
        elif number[i]=='4':
            cztery = cztery+1
        elif number[i]=='5':
            piec = piec+1
        elif number[i]=='6':
            szesc = szesc+1
        elif number[i]=='7':
            siedem = siedem +1
        elif number[i]=='8':
            osiem = osiem +1
        elif number[i]=='9':
            dziewiec = dziewiec+1
        else:
            return "Give me a number!"
    
    if jeden<2:
        jeden = 0
    if dwa<2:
        dwa=0
    if trzy<2:
        trzy = 0
    if cztery<2:
        cztery=0
    if piec<2:
        piec=0
    if szesc<2:
        szesc=0
    if siedem<2:
        siedem = 0
    if osiem<2:
        osiem = 0
    if dziewiec<2:
        dziewiec=0

    suma = jeden + dwa*2 +  trzy*3 + cztery*4 + piec*5 + szesc*6 + siedem*7 + osiem*8 + dziewiec*9

    return suma  


if __name__=="__main__":
    print(f(1027))
    print(f(230335))
    print(f(513553007))