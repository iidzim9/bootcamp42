# Python program to demonstrate
# sys.argv

import sys
import operator

n = len(sys.argv)
if n != 3:
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
else:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("Sum : %d" % (a+b))
        print("Difference : %d" % (a-b))
        print("Product : %d" % (a*b))
        print("Quotient : %d" % (a/b))
        print("Remainder : %d" % (a%b))
    else:
        print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

#  && arg[1].isdigit():