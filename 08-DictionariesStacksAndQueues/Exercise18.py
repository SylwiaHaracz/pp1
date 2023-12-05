"""with open("ICAO.txt", "w") as file:
    file.write('A Alfa \n')
    file.write('B Bravo \n')
    file.write('C Charlie \n')
    file.write('D Delta \n')
    file.write('E Echo \n')
    file.write('F Foxtrot \n')
    file.write('G Golf \n')
    file.write('H Hotel \n')
    file.write('I India \n')
    file.write('J Juliett \n')
    file.write('K Kilo \n')
    file.write('L Lima \n')
    file.write('M Mike \n')
    file.write('N November \n')
    file.write('O Oscar \n')
    file.write('P Papa \n')
    file.write('Q Quebec \n')
    file.write('R Romeo \n')
    file.write('S Sierra \n')
    file.write('T Tango \n')
    file.write('U Uniform \n')
    file.write('V Victor \n')
    file.write('W Whiskey \n')
    file.write('X Xray \n')
    file.write('Y Yankee \n')
    file.write('Z Zulu \n')"""

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

with open("ICAO.txt", "w") as file:
    for key,value in fonetic.items():
        file.write(f'{key.upper()} {value} \n')