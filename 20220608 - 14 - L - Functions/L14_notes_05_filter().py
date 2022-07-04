# 20220608 - Python Code - Functions - Lecture
# 05 - filter() with and without lambda function


# -------------- with lambda function --------------------------------------


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, numbers))

print(result, '- all the even numbers from the list')


# --------------- without lambda function ------------------------------------


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def check_numbers(num):
    if num % 2 == 0:
        result_1 = True
    else:
        result_1 = False

    return result_1


print(list(filter(check_numbers, numbers)))
