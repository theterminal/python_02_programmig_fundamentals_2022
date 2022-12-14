# 20220620 - Python - List Advanced - Exercise
# L18 - Note 01


print('\nMatrix with start value of 1, user specified end range, step value of 1, for column and row 1')
print('The rest of the matrix is the multiplication table of the column 1 with row 1\n')


working_range = range(1, int(input('Enter range end number: ')) + 1)
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


print('_____ example_2 _____prints table 10 * 10 _____\n')


lst_matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

for i in lst_matrix[0]:
    for j in lst_matrix[1]:
        if i * j < 10:
            print(f' {i * j}', end=' ')
        else:
            print(i * j, end=' ')
    print()
print()


print('_____ example_3 _____prints table 9 * 9 _____\n')


lst_matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]

for i in lst_matrix[0]:
    for j in lst_matrix[1]:
        if i * j < 10:
            print(f' {i * j}', end=' ')
        else:
            print(i * j, end=' ')
    print()
