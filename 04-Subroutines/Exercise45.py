def f(expression):
    suma = int(expression[0])
    for i in range (1,len(expression),2):
        if expression[i] =="+":
            suma = suma + int(expression[i+1])
        if expression[i] == "-":
            suma = suma - int(expression[i+1])
    return suma

if __name__=="__main__":
    print(f("2+3-4+5-0"))