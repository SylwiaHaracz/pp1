def number_of_words(text):
    arr = text.split()
    return(len(arr))

def ordered(text):
    arr = text.split()
    arr2=list(set(arr))
    arr3=sorted(arr2, key=len)
    return arr3[::-1]

def alphabet(text):
    arr = text.split()
    arr2=list(set(arr))
    return sorted(arr2, key=len)
