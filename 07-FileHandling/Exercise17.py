file = open("data.txt","r", encoding='utf-8')
for i in range (0,5):
    print(file.readline())
file.close()