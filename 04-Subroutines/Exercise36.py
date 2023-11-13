def f(detector):
    inside = 0
    for i in range (0, len(detector)):
        if detector[i]=="+":
            inside = inside + 1
            if inside==3:
                return True
                break
        elif detector[i]=="-":
            inside = inside - 1
    if inside<3:
        return False
    
if __name__=="__main__":
    print(f("+-+++-+---"))