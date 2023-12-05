word = input('Enter a word: ')
lowercase = word.lower()
letters = [*lowercase]

fonetic={
    "a":"Alfa",
    "b":"Bravo",
    "c":"Charlie",
    "d":"Delta",
    "e":"Echo",
    "f":"Foxtrot",
    "g":"Golf",
    "h":"Hotel",
    "i":"India",
    "j":"Juliett",
    "k":"Kilo",
    "l":"Lima",
    "m":"Mike",
    "n":"November",
    "o":"Oscar",
    "p":"Papa",
    "q":"Quebec",
    "r":"Romeo",
    "s":"Sierra",
    "t":"Tango",
    "u":"Uniform",
    "v":"Victor",
    "w":"Whiskey",
    "x":"Xray",
    "y":"Yankee",
    "z":"Zulu"
}

"""
for letter in letters:
    if letter =='a':
        print('Alfa', end=" ")
    elif letter =='b':
        print('Bravo', end=" ")
    elif letter =='c':
        print('Charlie', end=" ")
    elif letter =='d':
        print('Delta', end=" ")
    elif letter =='e':
        print('Echo', end=" ")
    elif letter =='f':
        print('Foxtrot', end=" ")
    elif letter =='g':
        print('Golf', end=" ")
    elif letter =='h':
        print('Hotel', end=" ")
    elif letter =='i':
        print('India', end=" ")
    elif letter =='j':
        print('Juliett', end=" ")
    elif letter =='k':
        print('Kilo', end=" ")
    elif letter =='l':
        print('Lima', end=" ")
    elif letter =='m':
        print('Mike', end=" ")
    elif letter =='n':
        print('November', end=" ")
    elif letter =='o':
        print('Oscar', end=" ")
    elif letter =='p':
        print('Papa', end=" ")
    elif letter =='q':
        print('Quebec', end=" ")
    elif letter =='r':
        print('Romeo', end=" ")
    elif letter =='s':
        print('Sierra', end=" ")
    elif letter =='t':
        print('Tango', end=" ")
    elif letter =='u':
        print('Uniform', end=" ")
    elif letter =='v':
        print('Victor', end=" ")
    elif letter =='w':
        print('Whiskey', end=" ")
    elif letter =='x':
        print('Xray', end=" ")
    elif letter =='y':
        print('Yankee', end=" ")
    elif letter =='z':
        print('Zulu', end=" ")"""


for letter in letters:
    for i in fonetic:
        if letter == i:
            print(fonetic[i], end=" ")