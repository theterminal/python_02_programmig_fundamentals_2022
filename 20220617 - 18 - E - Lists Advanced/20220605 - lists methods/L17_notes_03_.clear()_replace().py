# 20220615 - Python - Lists Advance - Lecture
# Notes - 02 - List Comprehensions


# -------------------------- .clear() --------------------------
print('\n\n----- ex. 1 ----- .clear() ---------------------\n\n')


lst_10 = [1, 2, 3]
print(lst_10, '     - original list')

lst_10.clear()
print(lst_10, '            - deletes all elements from the list')


# ------------------------- list(), filter(), lambda, comprehension -------------
print('\n\n----- ex. 2 ----- \'filter\', \'lambda\', \'comprehension\' -----\n\n')


lst_20 = [1, 2, 3, 4, 5]

print(list(filter(lambda x: x % 2 == 0, lst_20)), '    - using \'list\', \'filter\', \'lambda\'')
print([x for x in lst_20 if x % 2 == 0], '    - using \'comprehension\'')


# -------------------------- .replace(x, y) --------------------------
print('\n\n----- ex. 3 ----- .replace(x, y) ---------------------\n\n')


str_30 = '120Hello'
print(str_30)

num_in_str_30 = '120'
str_30 = str_30.replace(num_in_str_30, '')

print(str_30)

