# 20220529 - Python - Python Fundamentals - L9 - Data Types and Variables
# 06 - Next Happy Year - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#5

# ------------- version 3 --------------------------

from itertools import permutations

year_start = tuple(map(int, input()))
permutation_all = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(year_start))

for digit in list(permutation_all):                           # could be without encapsulating it in list()
    print(digit)
    if digit > year_start:
        happy_year = ''.join(str(x) for x in digit)
        print(happy_year)
        break

# ------------- version 2 --------------------------

# year_start = int(input())
#
# year_current = year_start
# happy_year = False
# length = len(str(year_start))
#
# while not happy_year:
#     year_current += 1
#     set_year = set()
#
#     for i in range(length):
#         set_year.add(str(year_current)[i])
#
#     happy_year = len(set_year) == length        # True / False statement
#
# print(year_current)

# -------------- version 1 ----------------------------

# year_start = int(input())
# happy_year = False
#
# while not happy_year:
#     year_start += 1
#     set_year = set()
#
#     for i in range(len(str(year_start))):
#         set_year.add(str(year_start)[i])
#
#     happy_year = len(set_year) == len(str(year_start))
#
# print(year_start)
