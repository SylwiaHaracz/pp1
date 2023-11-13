def f(dice):
    max=0
    result=0
    for i in dice:
        count =0
        for y in dice:
            if i==y:
                count +=1
            else:
                if count>max:
                    result = i
                    max = count
                count =0
            if count>max:
                result = i
                max = count
    return result

if __name__=="__main__":
    print(f('5233165554211'))