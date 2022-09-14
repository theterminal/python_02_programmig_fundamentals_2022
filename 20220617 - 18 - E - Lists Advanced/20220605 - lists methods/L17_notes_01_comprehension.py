# 20220615 - Python - Lists Advance - Lecture
# Notes - 01 - List Comprehension


# ------------------- 01 ------------------------------------------------------
print('\n\n------- ex. 1 -------------------------------------------------\n\n')


lst_10 = [0, 1, 2, 3, -4, 5, -6, 7, 8, -9]
lst_11 = [x**2 for x in lst_10 if x > 0]

print(lst_10, '     - original list')
print(lst_11, '                 - new list with satisfied condition')   # power of 2 of all elements '> 0' in the list


# ------------------- 02 -------------------------------------------------------
print('\n\n------- ex. 2 --------------------------------------------------\n\n')


print('Enter the string between the pipes: | -12 -5 0 8 11 45 9 |\n')
#      Enter the string between the pipes: | -12 -5 0 8 11 45 9 |

lst_20 = [int(x) for x in input().split() if int(x) <= 0]

print(lst_20, '         - returns a list of \'int\' elements \'<= 0\' from entered \'str\' elements')
# returns a list of 'int' elements '<= 0' from entered 'str' elements


# ------------------- 03 --------------------------------------------------------
print('\n\n------- ex. 3 ---------------------------------------------------\n\n')


print('Enter the string between the pipes: | -12 -5 0 8 11 45 9 |\n')
#      Enter the string between the pipes: | -12 -5 0 8 11 45 9 |

lst_30 = [int(x) for x in input().split() if int(x) <= 0 or int(x) + 3 == 12]

print(lst_30, '     - returned list with elements that satisfied the condition...')


# ------------------- 04 -------------------------------------------------------
print('\n\n------- ex. 4 ----- creating list from \'range\' ----------------\n\n')

lst_40 = [x for x in range(12)]

print(lst_40, '      - created with comprehension')
# returns the list 'lst_4' with the 'int' elements [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# ------------------- 05 -------------------------------------------------------
print('\n\n------- ex. 5 ---------------------------------------------------\n\n')

lst_50 = [1, -2, -3.78, 4, 5, 6, 7]

true_false = [True if x % 2 == 0 else False for x in lst_50]
print(true_false)
# returns: [False, True, False, True, False, True, False, True, False]


# ------------------- 06 -------------------------------------------------------
print('\n\n------- ex. 6 ---------------------------------------------------\n\n')

lst_50 = [1, -2, -3.78, 4, 5, 6, 7]

print([x if x % 2 == 0 else x * 1000 for x in lst_50])
print([x - 77 for x in [x if x % 2 == 0 else x * 1000 for x in lst_50]])
print([x - 77 for x in [x if x % 2 == 0 else x * 1000 for x in [1, -2, -3.78, 4, 5, 6, 7]]])

# study those examples
