age = float(input("Enter yhe dog's age in human years: "))
if age<=2:
    in_dog_years = age*10.5
    print(f"The dog's age in dog years is {in_dog_years}")
else:
    in_dog_years = 2*10.5 + (age-2)*4
    print(f"The dog's age in dog years is {in_dog_years}")