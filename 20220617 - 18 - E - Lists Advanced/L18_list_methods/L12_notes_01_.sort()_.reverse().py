# 20220603 - Python - L12 - Lists Basics - Exersice
# Notes 01


print('\n----- ex. 1 ----- .sort() -----\n')


# lst_10.sort()                            # sorts list in ascending order; works for nums and alpha
# lst_10.sort(reverse=True)                # sorts list in descending order; works for nums and alpha
# print(lst_10.sort)                       # cannot use this syntax (it returns None). Also, cannot assign it to a variable.


lst_10 = [2, 34, -4, 5, 0]
print(lst_10, '- Original list')

lst_10.sort()
print(lst_10, '- Same list sorted ascending')

lst_10.sort(reverse=True)
print(lst_10, '- Same list sorted descending')

print(lst_10.sort(), '             - Cannot use this syntax')


print('\n----- ex. 2 ----- .reverse() -----\n')


# list_20.reverse                           # reverses the list
# list_20[::-1]                             # reverses the list (using slicing)
# print(list_20.reverse()                   # cannot use this syntax (it returns None). Also, cannot assign it to a variable.


lst_20 = [2, 34, -4, 5, 0]
print(lst_20, '- Original list')

lst_20.reverse()
print(lst_20, '- Same list reversed')

print(lst_20[::-1], '- Same list reversed again using slicing')

print(lst_20.reverse(), '             - Cannot use this syntax.')
