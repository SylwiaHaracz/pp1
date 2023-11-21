arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

naj=len(arr[0])

for i in arr:
    if len(i)>naj:
        naj=len(i)

for i in arr:
    if len(i)==naj:
        print(i)