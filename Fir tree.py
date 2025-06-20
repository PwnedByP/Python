'''
You'll write a Python 3 program drawing a fir tree.

The size of the drawed fir tree will depend on the single parameter given to your program. As always, print a human error message if no parameter are given to your program.

Given 0, your program should display nothing.

https://genepy.org/exercises/sapin

I HAVEN'T DONE THIS EXERCISE, I TRIED AND I COULDN'T CHATGPT ANSWER BELOW, and it's still not the correct answer.
'''

import sys

def drawing(levels):
    star = "*"
    space = " "
    base_height = 4
    level = int(levels)

    # Compute actual width of the bottom line
    def compute_max_width(levels, base_height=4):
        stars = 1
        for l in range(levels):
            height = base_height + l
            for _ in range(height):
                stars += 2
            stars -= 4
        stars += 4
        return stars - 2

    max_width = compute_max_width(level)

    # Draw the tree
    start_stars = 1
    for l in range(level):
        height = base_height + l
        n_stars = start_stars
        for _ in range(height):
            print(space * ((max_width - n_stars) // 2) + star * n_stars)
            n_stars += 2
        start_stars = n_stars - 4

    # Draw the trunk
    trunk_width = 1 if level == 1 else 3
    trunk = "|" * trunk_width
    spaces = (max_width - trunk_width) // 2
    for _ in range(level):
        print(space * spaces + trunk)


drawing(sys.argv[1])