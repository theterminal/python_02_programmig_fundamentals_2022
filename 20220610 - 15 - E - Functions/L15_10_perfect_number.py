# 20220614 - Python Code - Functions - Exercise
# 10 - Perfect Number - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#9


# ----------------- version 1 --------------------


def perfect_number(num_1: int):
    sum_divisors = 0
    for i in range(1, int(num_1 / 2) + 1):
        if num_1 % i == 0:
            sum_divisors += i

    if num_1 == sum_divisors:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


num_to_test = int(input())
perfect_number(num_to_test)
