'''
As an introduction to sorting lists in Python you'll have to implement two functions.

In this exercise we represent students as a pair of (mark, full_name), so a tuple of two elements.

And in this exercises we represent students as lists of pairs.

Part 1:
Write a function named sort_by_mark that take as argument a list of students and returns a copy of it sorted by mark in descending order.

Part 2:
Write a function named sort_by_name that take as argument a list of students and returns a copy of it sorted by name in ascending order.

https://genepy.org/exercises/sort-students
'''

def sort_by_mark(my_class):
    return sorted(my_class, key=lambda my_class: my_class[0], reverse=True)


def sort_by_name(my_class):
    return sorted(my_class, key=lambda my_class: my_class[1])