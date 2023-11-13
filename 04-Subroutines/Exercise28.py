def f(binary_number):
    try:
        num = int(binary_number,2)
        return True
    except:
        return False

if __name__=="__main__":
    number = '123456'
    print(f'{number} is binary: {f(number)}')