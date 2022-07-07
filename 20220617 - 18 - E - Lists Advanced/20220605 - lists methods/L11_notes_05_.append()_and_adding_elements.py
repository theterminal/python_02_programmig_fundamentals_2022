# 20220604 - Python Code - L11 - Lists Basics
# Notes 05


# ------------------------ Adding element to a list NOT with append ----------
print('\n----- ex. 1 ----- Adding element to a list NOT with append() -----\n')


lst_10 = ['a', 'b', 'c']
print(lst_10)

for i in range(ord('d'), ord('z') + 1):
    lst_10 += [chr(i)]
print(lst_10)


# ------------------------ .append() -----------------------------------------
print('\n----- ex. 2 ----- .append() --------------------------------------\n')


# lst_20.append(value)                     # appends an element in the list, at the end, with the specified value (element)


lst_20 = [2, 34, -4, 5, 0]
print(lst_20, '          - Original list')

lst_20.append(4555)
print(lst_20, '    - Added 4555 to end of the list')


# ------------------------ .append() -----------------------------------------
print('\n----- ex. 3 ----- .append() --------------------------------------\n')


# lst_21.append(list_22.pop())             # takes the last element from list_22 and adds it as last element of list_21

lst_30 = [1, 2, 3]
lst_31 = [7, 8, 9]

lst_31.append(lst_30.pop())
print(lst_31, '- Takes the last element from \'lst_30\' and adds it as last element to \'lst_31\'')
