# 20220616 - Python Code - Lists Advance - Lecture
# from lecture - 01


# ----------------- version 1 ---------------------------------


import timeit


def even_numbers_with_comprehension():
    return [num for num in [1, 2, 3, 4, 5, 6]]


def even_numbers_with_loop():
    even_nums = []

    for num in [1, 2, 3, 4, 5, 6]:
        even_nums.append(num)

    return even_nums


print(timeit.timeit(even_numbers_with_comprehension))           # result ->  0.8331775270053186
print(timeit.timeit(even_numbers_with_loop))                    # result ->  0.703883087990107


# ------------------- version 2 --------------------------------


def even_numbers_with_comprehension():
    return [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]


def even_numbers_with_loop():
    even_nums = []

    for num in [1, 2, 3, 4, 5, 6]:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


print(timeit.timeit(even_numbers_with_comprehension))           # result ->  0.8797311710077338
print(timeit.timeit(even_numbers_with_loop))                    # result ->  0.7955889709992334


# -------------------------------------------------------------


print([x for x in range(11)])
print(list(range(11)))


# -------------------------- way to use longer numbers --------


print(100000 + 1000000)
print(100_000 + 1_000_000)


# --------------------------------------------------------------


print([num + 1 for num in range(23)])
