def f(name):
    space = name.split()
    wynik = ""
    for a in space:
        wynik = wynik + " " +(a[0])
    return wynik


if __name__=="__main__":
   print(f("Ala ma kota"))