# 20220618 - Python - Lists Advance - Lecture
# Notes - 07 - list(), set()


"""

The 'set' type is unordered data type and has no indexes.
It contains unique elements.

"""


print('\n\n------ ex. 1 ----- list(set())----------\n\n')


lst_10 = [77, 77, 2, 3, 3, 3, 4, 5, 6, 6, 6]
print(lst_10)                                                 # [77, 77, 2, 3, 3, 3, 4, 5, 6, 6, 6]

set_10 = set(lst_10)
print(set_10)                                                 # {2, 3, 4, 5, 6, 77}


print('\n\n------ ex. 2 ----- list(set())----------\n\n')


set_20 = set('This is a sample set')
print(set_20)                                                 # {'i', 'p', 'a', 'e', 'T', 'm', 't', 'l', ' ', 'h', 's'}

set_21 = {44, 0, 7, 7, 7, 3, 3, 3}
print(set_21)                                                 # {0, 3, 44, 7}
