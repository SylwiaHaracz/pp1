def occurs(number, array):
    if number in array:
        return True
    else:
        return False
    
if __name__=="__main__":
    num = int(input('Enter a number: '))
    print(occurs(num, [15, 38, 7, 23, 14]))