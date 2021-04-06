# Python program to demonstrate
# sys.argv

import sys
import operator

n = len(sys.argv)
if n != 3:
    if n < 3:
        print("InputError: add more arguments\n")
    elif n > 3:
        print("InputError: too many arguments\n")
    print("Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")
else:
    if sys.argv[1].isdecimal() and sys.argv[2].isdecimal():
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("Sum : %d" % (a+b))
        print("Difference : %d" % (a-b))
        print("Product : %d" % (a*b))
        if a == 0 or b == 0:
            print("Quotient : ERROR (div by zero)")
            print("Remainder : ERROR (div by zero)")
        else:
            print("Quotient : %d" % (a/b))
            print("Remainder : %d" % (a%b))
    else:
        print("InputError: only numbers\n\nUsage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3")

#  && arg[1].isdigit():