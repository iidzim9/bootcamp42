# Python program to demonstrate
# sys.argv

import sys

n = len(sys.argv)
word = ""
car = ''
for i in reversed(range(1, n)):
    s = len(str(sys.argv[i]))
    for j in reversed(range(0, s)):
        c = sys.argv[i][j]
        if c.islower():
            c = c.upper()
        else:
            c = c.lower()
        word += c
    if i > 1:
        word += " "
print(word, end="")
