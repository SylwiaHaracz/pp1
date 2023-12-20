def avg_speed(s, h, min):
    t=h+min/60
    v = s/t
    return round(v,2)

print(avg_speed(70, 1, 23))