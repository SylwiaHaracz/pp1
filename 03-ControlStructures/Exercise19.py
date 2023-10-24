sum = 0
i=1
while i<=10:
    if i%2 == 0:
        sum+=i
        i+=1
    else:
        i+=1
    
print(f'Suma = {sum}')