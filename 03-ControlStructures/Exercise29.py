washing_product = "shoes"
rinse = True
spin = False

if washing_product == "jacket":
    time = 40
    if rinse:
        time = time+15
    if spin:
        time = time+9
if washing_product == "underwear":
    time = 70
    if rinse:
        time = time+15
    if spin:
        time = time+9
if washing_product == "shoes":
    time = 20
    if rinse:
        time = time+15
    if spin:
        time = time+9

print(f'Total washing time: {time} minutes')