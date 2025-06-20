'''
Write a program that print the result of simple addition.
If no parameters are given, you must print the following error message:

usage: python3 solution.py OP1 OP2

https://genepy.org/exercises/my-add
'''

import sys

if len(sys.argv) != 3:
    print ("usage: python3 solution.py OP1 OP2")
elif (sys.argv[1]).isdigit() and (sys.argv[2]).isdigit():
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("usage: python3 solution.py OP1 OP2")