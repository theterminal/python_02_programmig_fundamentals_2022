# 20220614 - Python - Functions - Exercise
# 07 - Mim Max and Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#6


# ------------------- version 2 ----------------------- judge 100%


lst_nums = [int(i) for i in input().split()]
print(f'The minimum number is {min(lst_nums)}')
print(f'The maximum number is {max(lst_nums)}')
print(f'The sum number is: {sum(lst_nums)}')


# ------------------- version 1 ----------------------- judge 100%


def min_max_sum(lst_ints: list):
    min_num = min(lst_ints)
    max_num = max(lst_ints)
    sum_all_nums = sum(lst_ints)

    return f'The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_all_nums}'


lst_nums = [int(i) for i in input().split()]
result = min_max_sum(lst_nums)
print(result)
