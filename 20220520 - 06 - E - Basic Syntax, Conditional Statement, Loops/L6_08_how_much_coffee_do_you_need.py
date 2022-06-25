# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 08 - How Much Coffee Do You Need? - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#7


# -------------------------- version 5 -------------------------------------------


counter_coffee = 0

while True:
    str_to_test = input()
    if str_to_test == 'END':
        break

    words = ['coding', 'movie', 'dog', 'cat']

    for i in words:
        if str_to_test == i.lower():
            counter_coffee += 1
        elif str_to_test == i.upper():
            counter_coffee += 2

if counter_coffee > 5:
    print('You need extra sleep')
else:
    print(counter_coffee)


# -------------------------- version 4 ------------------------------------------


counter_coffee = 0

while True:
    str_to_test = input()
    if str_to_test == 'END':
        break

    words_l = ['coding', 'movie', 'dog', 'cat']
    words_u = ['CODING', 'MOVIE', 'DOG', 'CAT']

    if str_to_test in words_l:
        counter_coffee += 1
    elif str_to_test in words_u:
        counter_coffee += 2

if counter_coffee > 5:
    print('You need extra sleep')
else:
    print(counter_coffee)


# -------------------------- version 3 -------------------------------------------


counter_coffee = 0

while True:
    str_to_test = input()
    if str_to_test == 'END':
        break

    if str_to_test.lower() == 'coding' \
            or str_to_test.lower() == 'movie' \
            or str_to_test.lower() == 'dog' \
            or str_to_test.lower() == 'cat':

        if str_to_test.islower():
            counter_coffee += 1
        else:
            counter_coffee += 2

if counter_coffee > 5:
    print('You need extra sleep')
else:
    print(counter_coffee)


# -------------------------- version 2 -------------------------------------------


counter_coffee = 0
flag = False

while True:
    str_to_test = input()
    if str_to_test == 'END':
        break

    if str_to_test.isupper():
        flag = True
    str_to_test = str_to_test.lower()

    if str_to_test == 'coding'\
            or str_to_test == 'movie'\
            or str_to_test == 'dog'\
            or str_to_test == 'cat':

        if flag:
            counter_coffee += 2
        else:
            counter_coffee += 1

    flag = False

if counter_coffee > 5:
    print('You need extra sleep')
else:
    print(counter_coffee)


# -------------------------- version 1 ------------------------------------------


counter_coffee = 0

while True:
    str_to_test = input()
    if str_to_test == 'END':
        break

    if str_to_test == 'coding' or str_to_test == 'movie' or str_to_test == 'dog' or str_to_test == 'cat':
        counter_coffee += 1
    if str_to_test == 'CODING' or str_to_test == 'MOVIE' or str_to_test == 'DOG' or str_to_test == 'CAT':
        counter_coffee += 2

if counter_coffee > 5:
    print('You need extra sleep')
else:
    print(counter_coffee)
