# 20220529 - Python - Python Fundamentals - L9 - Data Types and Variables
# 06 - Next Happy Year - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#5


# ------------- version 3 -------------------------- judge: 100%


from itertools import permutations

year_start = tuple(map(int, input()))
permutation_all = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(year_start)))

for permutation in permutation_all:                          # could be without encapsulating it in list()
    if permutation > year_start:
        happy_year = ''.join(str(x) for x in permutation)
        print(happy_year)
        break


# ------------- version 2 -------------------------- judge: 100%


year_start = int(input())

year_current = year_start
happy_year = False
length = len(str(year_start))

while not happy_year:
    year_current += 1
    set_year = set()

    for i in range(length):
        set_year.add(str(year_current)[i])

    happy_year = len(set_year) == length        # it turns the flag to 'True' if 'len(set_year) == length'

print(year_current)


# -------------- version 1 ------------------------- judge: 100%


year_start = int(input())
happy_year = False

while not happy_year:
    year_start += 1
    set_year = set()

    for i in range(len(str(year_start))):
        set_year.add(str(year_start)[i])

    happy_year = len(set_year) == len(str(year_start))

print(year_start)


""" ------------------- Next Happy Year -------------------


You are saying goodbye to your best friend: "See you next happy year".
Happy Year is the year with only distinct digits, for example, 2018.
Write a program that receives an integer number and finds the next happy year.


---------- Test Data ------------


Input 1:            Output 1:
-------             --------
8989                9012


---------------------------------


Input 2:            Output 2:
-------             --------
1001                1023


---------------------------------


"""
