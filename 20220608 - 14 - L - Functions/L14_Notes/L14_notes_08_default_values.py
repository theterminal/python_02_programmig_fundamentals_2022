# 20220608 - Python - Functions - Lecture
# 08 - Default Values - Keyword Arguments and Position Arguments


# -------- keyword arguments 1 --------------------


def first_last_name(first='George', last='Brown'):
    print(first, last)


first_last_name("Milano")
first_last_name('Tesla, Ford')
first_last_name('Nikola Tesla, Ford')
first_last_name('Nikola Tesla', 'Ford')


# --------- keyword arguments 2 --------------------


def name_test(first, last='Smith'):                 # cannot place  [ last='Smith' ]  - keyword arguments must be last in the definition of the function
    return f'Hello, {first} {last}'


print(name_test('Ivan', 'Ivanov'))
print(name_test('Ivan'))


# -------- position arguments 01 ---------------------


def calculate_area(width, height):
    result = width * height
    return result


print(calculate_area(3, 5))


# -------- position arguments 02 ---------------------


def calculate_area(width, height):
    result = width * height
    return result


print(calculate_area(height=5, width=3))
