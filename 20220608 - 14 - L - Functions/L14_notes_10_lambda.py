# 20220608 - Python Code - Functions - Lecture
# 10 - Using Lambda

# ------- using lambda function ----------------


x = lambda a, b, c: (a + 10) * b + c
print(x(5, 3, 1))


# ----------------------------------------------


full_name = lambda first, last: f'I am {first} {last}'

result = full_name('Guido', 'van Rossum')

print(result)                                           # I am Guido van Rossum


# ----------------------------------------------


result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8]))
print(result)                                                               # [2, 4, 6, 8]


# ----------------------------------------------


result = list(filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8]))
print(result)                                                               # [1, 3, 5, 7]


# ----------------------------------------------


result = list(map(lambda x: x % 2 == 0, [1, 2, 3, 4]))
print(result)                                                               #[False, True, False, True]


# ----------------------------------------------


result = list(map(lambda x: x % 2, [1, 2, 3, 4]))
print(result)                                                                # [1, 0, 1, 0]
