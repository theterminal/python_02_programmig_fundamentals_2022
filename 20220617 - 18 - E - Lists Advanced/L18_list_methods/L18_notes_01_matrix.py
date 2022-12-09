# 20220620 - Python - List Advanced - Exercise
# Notes 01


# prints table 25 * 25
working_range = range(int(input('\nEnter range start number: ')), int(input('Enter range end number: ')) + 1, int(input('Enter stet: ')))

lst_matrix = [[i for i in working_range], [i for i in working_range]]
print()

for i in lst_matrix[0]:
    for j in lst_matrix[1]:
        if i * j < 10:
            print(f'  {i * j}', end=' ')
        elif i * j < 100:
            print(f' {i * j}', end=' ')
        else:
            print(i * j, end=' ')
    print()
print()


# prints table 10 * 10
lst_matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

for i in lst_matrix[0]:
    for j in lst_matrix[1]:
        if i * j < 10:
            print(f' {i * j}', end=' ')
        else:
            print(i * j, end=' ')
    print()
print()


# prints table 9 * 9
lst_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

for i in lst_matrix[0]:
    for j in lst_matrix[1]:
        if i * j < 10:
            print(f' {i * j}', end=' ')
        else:
            print(i * j, end=' ')
    print()
