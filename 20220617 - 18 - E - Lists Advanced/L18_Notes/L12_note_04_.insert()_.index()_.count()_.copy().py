# 20220603 - Python - L12 - Lists Basics - Exersice
# Note 04


print('\n\n----- ex. 1 ----- .insert(index, element) --------------------\n\n')


# lst.insert(5, 'George')                           # inserts 'George' into the list on index 5


lst_10 = [2, 34, -4, 5, 0]
print(lst_10, '               - original list')

lst_10.insert(3, 'George')
print(lst_10, '     - the list after insertion')


print('\n\n----- ex. 2 ----- .index(value) ------------------------------\n\n')


# lst.index(34)                                    # returns the index of the specified element
# lst.index('a3')                                  # returns the index of the specified element


lst_20 = [2, 34, -4, 5, 0]
print(lst_20, '- original list')

num = lst_20.index(34)
print(num, '                - the \'index\' of the specified element')


print('\n\n----- ex. 3 ----- .index(value) ------------------------------\n\n')


# str.index('value')                               # returns the start 'index' of the specified value


str_30 = 'The string is: Jerry is really smart!'

print('"', str_30, '"', '- original string')
print(str_30.index('Jerry'), '                                       - the start index of the string entered in the search')

print('\nIt trows an exception if the value is not found.')


print('\n\n----- ex. 4 ----- .index(value) ------------------------------\n\n')


# lst.index(7)                                    # returns the start 'index' of the specified value


lst_40 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst_40, '         - original list')
print(lst_40.index(7), '- start index of the specified value from the list')


print('\n\n----- ex. 5 ----- .count(element) ----------------------------\n\n')


# lst.count(5)                                     # counts how many times the specified element (5) exist in the list


lst_50 = [2, 5, -4, 5, 0]
print(lst_50, '  - original list')

repetition = lst_50.count(5)
print(repetition, '                 - returns the count of the element with value \'5\' in the list')


print('\n\n----- ex. 6 ----- .copy() -----------------------------------\n\n')


# lst_2 = lst_1.copy()                             # creates new list 'lst_2' which is exact copy of 'lst_1'


lst_60 = [2, 34, -4, 5, 0]
print(lst_60, '     - \'lst_60\' - original list')

lst_61 = lst_60                                    # it does not copy the list only points to it in the memory
print(lst_61, '     - \'lst_61\' after \'lst_61 = lst_60\' - looks identical but if you change one of the list elements, it\'ll change both')

print(lst_61.pop(), '                     - that is the popped element from the lst_61. After that lst_62 is a copy of lst_60. It is visible that the lst_60 has been changed!')

lst_62 = lst_60.copy()                             # that is the correct way to do it.
print(lst_62, '        - \'lst_62\' after \'lst_62 = lst_60.copy\' - that creates completely independent instance from \'lst_60\'')
