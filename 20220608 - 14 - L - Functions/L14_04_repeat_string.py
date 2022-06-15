# 20220614 - Python Code - Functions - Lecture
# 04 - Repeat String - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#3

# ------- normal function ---------------------


def repeat_string(str_1, counter_1):
    result_1 = str_1 * counter_1

    return result_1


p1 = input()
p2 = int(input())
print(repeat_string(p1, p2))


# ------- using lambda function ----------------


result_2 = lambda a, b: a * b


str_in = input()
count = int(input())
print(result_2(count, str_in))


# ----------------------------------------------

