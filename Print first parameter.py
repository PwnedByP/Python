'''
Write a script that print the first parameter given to the script.

If there is no parameters given, it should print the following error message on stdout:

usage: python3 solution.py PARAM

https://genepy.org/exercises/print-the-first-parameter
'''

import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("usage: python3 solution.py PARAM")