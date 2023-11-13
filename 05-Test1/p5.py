def f(binary_number):
    for i in binary_number:
        if i =="1" or i =="0":
            continue
        else:
            return False
            break
    return True
    
if __name__=="__main__":
    print(f('1010100111'))