'''
Write a program that do basic calculations.

You need to be able to get basic operators such as +, - , *, /, % (modulo) and ^ (Exponentiation). Input will be integer numbers.

Your program will give a usage message if you don't give the three parameters.

For every other errors like if an operand is not an integer, you'll print an input error.

https://genepy.org/exercises/calculator1
'''

import sys

if len(sys.argv) != 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
else:
    if sys.argv[1].isdigit() and sys.argv[3].isdigit():
        x = int(sys.argv[1])
        y = int(sys.argv[3])
        try:
            match (sys.argv[2]):
                case "+":
                    print (x + y)
                case "-":
                    print (x - y)
                case "*":
                    print (x * y)
                case "/":
                    print (x / y)
                case "%":
                    print (x % y)
                case "^":
                    print (x ** y)
                case _:
                    print ("input error")
        except:
            print("input error")
    else:
        print ("input error")

