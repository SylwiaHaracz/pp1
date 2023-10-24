a= 4
b=15
for i in range (1,b+1):
    print("*", end=" ")
print('\r')
for j in range (1,a+1):
    print("*", " "*((b-2)*2), "*")
for i in range (1,b+1):
    print("*", end=" ")