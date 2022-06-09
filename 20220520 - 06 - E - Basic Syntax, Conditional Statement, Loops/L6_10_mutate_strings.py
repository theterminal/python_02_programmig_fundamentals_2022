# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 10 - Mutate Strings - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#9

# ------------------- version 2 -------------------------------- KK

str_1, str_2 = input(), input()
last_str_printed = str_1

for i in range(len(str_1)):
    part_l = str_2[: i + 1]
    part_r = str_1[i + 1: len(str_1)]
    word_to_print = part_l + part_r

    if last_str_printed == word_to_print:
        continue
    else:
        last_str_printed = word_to_print
        print(last_str_printed)

# ------------------- version 1 -------------------------------- KK

str_1, str_2 = input(), input()
word_to_print = ''

for i in range(len(str_1)):
    if str_1[i] != str_2[i]:
        word_to_print += str_2[i]
        print(word_to_print + str_1[i + 1: len(str_1)])
    else:
        word_to_print += str_1[i]
