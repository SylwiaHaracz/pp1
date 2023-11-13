def f(n):
    wynik = ""
    for n in range (1,n+1):
        wynik = wynik + str(n)
    return wynik

if __name__=="__main__":
    print(f(12))