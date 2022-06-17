# 20220608 - Python Code - Functions - Lecture
# 07 - Addition, Subtraction, Recourse


# ------- operations with numbers -------------------------


def sum_fun(a, b):
    return a + b


def subtract_fun(a, b):
    return a - b


def operations_w_nums(a, b):
    print(f'Sum function result: {sum_fun(a, b)}')
    print(f'Subtract function result: {subtract_fun(a, b)}')


operations_w_nums(5, 1)


# ------- recourse --- countdown example ------------------


def countdown(num):
    print(num, end=', ')

    if num == 0:
        return
    else:
        countdown(num - 1)


countdown(10)
