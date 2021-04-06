# Python program to demonstrate
# sys.argv

from sys import argv 

n = len(argv)
word = ""
car = ''
for i in reversed(range(1, n)):
    s = len(str(argv[i]))
    for j in reversed(range(0, s)):
        c = argv[i][j]
        if c.islower():
            c = c.upper()
        else:
            c = c.lower()
        word += c
    if i > 1:
        word += " "
print(word, end="")


# out = word.swapcase()