# 20220603 - Python - L12 - Lists Basics - Exersice
# Notes 03


# ------------------------ .pop() ---------------------
print('\n----- ex. 1 ----- .pop() ------------------\n')


# lst_10.pop()                             # deletes the last element from the list, returns the deleted (popped) element
# a = lst_10.pop()                         # 'a' takes the value of the popped element
# lst_10.pop(4)                            # deletes and returns the element with the specified index


lst_10 = [2, 34, -4, 5, 0]
print(lst_10, '- original list')

lst_10.pop()
print(lst_10, '   - removes the last element from the list')

lst_10.pop(1)
print(lst_10, '       - removes the element with the specified index from the list, and returns its value')

print(lst_10.pop(), '                - prints out the deleted element from the list')

print(lst_10, '          - the list after the above operations')

print('\n\'.pop()\' is similar to \'.remove()\' but \'.remove()\' does NOT return the element that is being deleted. It returns \'None\'')


# ------------------------ del lst[index] ------------
print('\n----- ex. 2 ----- del lst[index] ----------\n')


# del lst[7]                                # deletes the element with the index 7


lst_20 = [2, 34, -4, 5, 0]
print(lst_20, '   - original list')

del lst_20[3]
print(lst_20, '      - deletes the element with index 3')


# ------------------------ .remove() ---------------
print('\n----- ex. 3 ----- .remove() --------------\n')


# lst.remove(10)                            # removes the element with the specified value


lst_30 = ['a', 'b', 'c']
lst_30.remove('b')

print(lst_30)


# ------------------------ .remove() ---------------
print('\n----- ex. 4 ----- .remove() --------------\n')


# lst.remove(10)                        # removes the element with the specified value


lst_40 = [5, 10, -12, 25, 0]
print(lst_40, '  - original list')

lst_40.remove(10)
print(lst_40, '      - the list after removing the element with value 10')
