# 20220614 - Python Code - Functions - Exercise
# 01 - Smallest of Three Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#0


# --------- version 1 ----------------------------------


def smallest_of_three_numbers(a: int, b: int, c: int):
    result = min(a, b, c)

    return result


p1 = int(input())
p2 = int(input())
p3 = int(input())
print(smallest_of_three_numbers(p1, p2, p3))


# --------- version 2 ----------------------------------


def smallest_of_three_numbers(a: int, b: int, c: int):
    return min(a, b, c)


p1 = int(input())
p2 = int(input())
p3 = int(input())
print(smallest_of_three_numbers(p1, p2, p3))


# --------- version 3 ----------------------------------


def smallest_of_three_numbers(lst_nums):
    return min(lst_nums)


p1 = int(input())
p2 = int(input())
p3 = int(input())

lst_all_nums = [p1, p2, p3]
min_num = smallest_of_three_numbers(lst_all_nums)
print(min_num)
