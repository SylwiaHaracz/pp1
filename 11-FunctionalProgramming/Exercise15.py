text = "I completely agree with you"
words = text.split()

result = list(map(lambda x: len(x), words))

print(result)