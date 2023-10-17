h = int(input("Enter hours\n"))
rate = int(input("Enter rate\n"))
pay = h*rate

if h>=40:
    higher_pay  = h*(1.5*rate)
    print(f"Pay gross: {higher_pay}")
    
else:
    print(f"Pay gross: {pay}")