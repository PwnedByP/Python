'''
Write a program that searches for common lines between multiple given files.

Your program accepts file names as parameters in sys.argv).

If no file are given, your program must print some help, then exit with a return code greater than zero.

If no lines are common between the given files, your program must exit with an error code greater than zero.

https://genepy.org/exercises/common-lines
'''

import sys

if len(sys.argv) < 2:
    sys.stderr.write("Usage: python3 Common_lines.py file1.txt file2.txt ...\n")
    sys.exit(1)

contents = []

for file in sys.argv[1:]:
    with open(file) as f:
        lines = {line.strip() for line in f if line.strip()}
        contents.append(lines)

duplicates = set.intersection(*contents)

for line in duplicates:
    print(line)

sys.exit(0 if duplicates else 1)



'''

Trying to do it using dictionaries:


import sys

lines = {}
line = 0
n_file = 1

for file in sys.argv[1:]:
    with open(file) as f:
        for l in f:
            line += 1
            content = l.rstrip()
            if content == "":
                continue
            if content in lines:
                lines[content].append(f"file: {n_file} line: {line}")
            else:
                lines[content] = [f"file: {n_file} line: {line}"]
    line = 0
    n_file += 1

for content, locations in lines.items():
    if len(locations) > 1:
        print(content,locations)
        
'''