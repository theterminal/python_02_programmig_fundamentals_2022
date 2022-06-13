# 20220601 - Python Code - L11 - Lists Basics
# Notes 02

# ----- creating a list from range-------------------------------
print('\nCreating a list from range')

lst_1 = list(range(1, 10))
print(lst_1)

print(list(range(1, 10)))

# ----- list from range with a step (pos, neg, ...) -------------
print('\nList from range with a step (pos, neg, ...)')

lst_1 = list(range(100, 1, -15))
print(lst_1)

print(list(range(200, -50, -25)))


# ------ creating a list form a range and joining it into a string --------------------------------------

print('\n---------- creating a list form a range and joining it into a string ---------------\n')

lst_1 = [n for n in range(1, 11)]

print(lst_1)
print(type(lst_1))
print(type(lst_1[0]))
print()

str_1 = ', '.join(str(lst_1[i]) for i in range(len(lst_1)))

print(str_1)
print(type(str_1))
print(type(str_1[0]))
