# 20220715 - Python Code - String Processing - Exercise
# 02 - Character Multiplier - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#1


# ------------------------ version 2 -------------------- judge: 100%


str_1, str_2 = input().split(' ')

n = max(len(str_1), len(str_2))
str_short = str_1
str_long = str_2
total = 0

if not (len(str_1) == len(str_2)):
    if len(str_1) < n:
        str_short = str_1
        str_long = str_2
    elif len(str_2) < n:
        str_short = str_2
        str_long = str_1

    for i in range(n):
        if i >= len(str_short):
            total += ord(str_long[i])
        else:
            total += (ord(str_long[i]) * ord(str_short[i]))
else:
    for i in range(n):
        total += (ord(str_long[i]) * ord(str_short[i]))

print(total)


# ------------------------ version 1 -------------------- judge: 100%


# string_1, string_2 = input().split(' ')
#
# n = max(len(string_1), len(string_2))
# str_shorter = string_1
# str_longer = string_2
# total = 0
#
# if not (len(string_1) == len(string_2)):
#     if len(string_1) < n:
#         str_shorter = string_1
#         str_longer = string_2
#     elif len(string_2) < n:
#         str_shorter = string_2
#         str_longer = string_1
#
#     for i in range(n):
#         if i >= len(str_shorter):
#             total += ord(str_longer[i])
#         else:
#             total += (ord(str_longer[i]) * ord(str_shorter[i]))
# else:
#     for i in range(n):
#         total += (ord(str_longer[i]) * ord(str_shorter[i]))
#
# print(total)
