# 20220615 - Python - Lists Advance - Lecture
# Note - 02 - .append(), .expend(), .insert()


print('\n\n----- ex.1 ----- .append() -----------------\n\n')


lst_10 = [1, 2, 3]
print(lst_10, '           - original list')

num_to_add = 4
lst_10.append(num_to_add)

print(lst_10, '        - adds the given element to the end of the list')


print('\n\n----- ex.2 ----- .append() -----------------\n\n')


lst_20 = [1, 2, 3]
print(lst_20, '           - original list')

num_to_add = 4
lst_20 += [num_to_add]               # must be in [] for it ot work

print(lst_20, '        - adds the given element to the end of the list !!! see the syntax')


print('\n\n----- ex.3 ----- .extend() -----------------\n\n')


lst_30 = [1, 2, 3]
print(lst_30, '           - original list')

lst_30.extend([4, 5])
print(lst_30, '     - adds the given elements to the end of the list')


print('\n\n----- ex.4 ----- .insert() -----------------\n\n')


lst_40 = [1, 2, 3]
print(lst_40, '           - original list')

lst_40.insert(1, 49)
print(lst_40, '       - adds the given element to the specified index')
