def stars(n):
    for i in range(0,n):
        print("*", end="")




arr=[12, 6, 4, 9, 10]

for i in arr:
    print(f'{i} -', end=" "), stars(i)
    print()