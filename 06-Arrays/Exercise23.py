arr=[-15, 8, -31, 47, -2, 19]

minimum=arr[0]
maksimum=arr[0]

for i in arr:
    if i<minimum:
        minimum=i
    if i>maksimum:
        maksimum=i

print(f'Minimum: {minimum}, Maksimum: {maksimum}')