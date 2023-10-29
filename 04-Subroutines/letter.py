def how_many(x):
    word = input('Enter a sentence: ')
    count = 0
    for letter in word:
       if letter == x:
          count = count + 1
    return count

if __name__=="__main__":
   a = input('Enter a letter you want to check: ')
   print(how_many(a))