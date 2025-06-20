'''
Write a flatten function, which given a list of lists (of any depth) returns a flattened version of it.

https://genepy.org/exercises/flatten-lists
'''

def flatten(a_list):
    flat_list = []
    for item in a_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

'''
Test
z = [1, [2, 3], [[4], 5]]

print(flatten(z))
'''