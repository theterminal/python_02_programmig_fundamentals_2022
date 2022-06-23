# 20220601 - Python Code - L11 - Lists Basics
# Notes 01


# -------------------------------------------------------------------------------------------------
print('\n\n----- ex. 1 ------ Creating a list and printing all elements ----------------------\n\n')


lst_10 = ['dog', 'cat', 'fish']

for element in lst_10:
    print(element)


# --------------------------------------------------------------------------------------------------
print('\n\n----- ex. 2 ------ Creating a list, printing all elements index and value ----------\n\n')


lst_20 = ['dog', 'cat', 'fish']

for i in range(len(lst_20)):
    print(i, end=" - ")
    print(lst_20[i])


# --------------------------------------------------------------------------------------------------
print('\n\n----- ex. 3 ------ Creating a list, printing all elements index and values ---------\n\n')


lst_30 = ['dog', 'cat', 'bird']

for i, v in enumerate(lst_30):
    print(i, v)


# --------------------------------------------------------------------------------------------------
print('\n\n----- ex. 4 ------ Creating a List and using \'in\' and \'not in\' ------------\n\n')


lst_40 = ['dog', 'cat', 'fish']

if 'dog' in lst_40:
    print('Yes! Dog is in')
else:
    print('0')


if 'Ivan' not in lst_40:
    print('No! Ivan is not in')
else:
    print('00')
