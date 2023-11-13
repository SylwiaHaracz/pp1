def f(name):
    lista = name.split()
    result = ""
    for i in lista:
        result =result + i[0]
    return result
        

if __name__=="__main__":
    print(f("Internet of Things"))