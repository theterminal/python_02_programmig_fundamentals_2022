# 20220601 - Python Code - L11 - Lists Basics
# Notes - Some Basic Syntax

# -----------------------------------
print('\n----------- Creating a List and printing its elements ------------\n')

lst_1 = ['dog', 'cat', 'fish']

for element in lst_1:
    print(element)

# -----------------------------------
print('\n----------- Creating a List and printing its elements index and values ------------\n')

lst_2 = ['dog', 'cat', 'fish']

for i in range(len(lst_2)):
    print(i, end=" - ")
    print(lst_2[i])

# -----------------------------------
print('\n----------- Creating a List and printing its elements index and values ------------\n')

lst_3 = ['dog', 'cat', 'bird']

for i, v in enumerate(lst_3):
    print(i, v)

# -----------------------------------
print('\n----------- Creating a List and using \'in\' and \'not in\' ------------\n')

lst_4 = ['dog', 'cat', 'fish']

if 'dog' in lst_4:
    print('Yes! Dog is in')
else:
    print('0')


if 'Ivan' not in lst_4:
    print('No! Ivan is not in')
else:
    print('00')
