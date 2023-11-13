def f(number1,number2,operator):
    if operator == "+":
        suma = number1 + number2 
        return suma
    elif operator == "-":
        odejmowanie = number1 - number2
        return odejmowanie
    elif operator =="*":
        mnożenie  = number1 * number2
        return mnożenie
    elif operator =="%":
        modulo = number1 % number2
        return modulo
    elif operator == "**":
        potegowanie = number1 ** number2
        return potegowanie
    else:
        return "Podaj właściwy operator"
    
if __name__=="__main__":
    print(f(2,3, "+"))
    print(f(2,3, "%") )
    print(f(2,3, "**") )
    print(f(2,3, "*") )
    print(f(2,3, "-") )