# 20220612 - Python Code

# ------------- .casefold()

str_1 = 'This is a test string'
print(str_1.casefold())

# ------------- .center()

str_2 = ' This is a second test string '
print(str_2.center(120, '-'))


# ------------- .find()
print('\n--- .find() --- \nIt returns -1 if the value is not found. That is the difference with .index()')

str_3 = 'This is a string 3 and it is a test.'
print(str_3.find('and'))


# ------------- .index()
print('\n--- .index() --- \nIt trows an exception if the value is not found. That is the only difference with .index()')

str_4 = 'This is a string 4. Ceci e lud!'
print(str_4.index('Ceci'))


