h = (input("Enter hours\n"))
rate = (input("Enter rate\n"))

try:
    h= int(h)
    rate = int(rate)
    if h>=40:
        higher_pay  = h*(1.5*rate)
        print(f"Pay gross: {higher_pay}")
    else:
        pay = h*rate
        print(f"Pay gross: {pay}")

except:
    print("Error, please enter numeric number")