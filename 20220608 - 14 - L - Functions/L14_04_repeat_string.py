# 20220614 - Python Code - Functions - Lecture
# 04 - Repeat String - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#3


# ------- normal function ---------------------


# def repeat_string(str_a1, counter_a2):
#     result = str_a1 * counter_a2
#
#     return result
#
#
# a1 = input()
# a2 = int(input())
#
# print(repeat_string(a1, a2))


# ------- using lambda function ----------------


result_2 = lambda x, y: x * y

x1 = input()
counter_y = int(input())

print(result_2(x1, counter_y))
