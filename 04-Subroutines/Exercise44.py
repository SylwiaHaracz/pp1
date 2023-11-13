def f(password):
    different = []
    if len(password)<6:
        return False
    for i in password:
        if i not in different:
            different.append(i)
    if len(different)>=6:
        return True
    else:
        return False
    

if __name__=="__main__":
    print(f("boook12"))