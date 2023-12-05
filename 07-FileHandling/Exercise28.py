import re
file = open("countries.txt", "r")
file_content = file.read()
letters = re.findall("[a-zA-Z]{6,}", file_content)
print(letters)