def f(text):
    if len(text)<=1:
        return text
    tekst = text[0]
    for i in text:
        tekst = tekst + i + "-"
    return tekst[1:-1]

if __name__=="__main__":
    print(f('University'))