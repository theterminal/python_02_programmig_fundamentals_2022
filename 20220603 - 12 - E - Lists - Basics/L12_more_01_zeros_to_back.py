# 22020613 - Python - L12 - Lists Basics - More Exercise
# 01 - Zeros to Back - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#0


# --------------------- version 1 --------------------------- judge 100%


lst_nums = [int(i) for i in input().split(', ')]

for i in lst_nums:
    if i == 0:
        lst_nums.remove(0)
        lst_nums.append(0)

print(lst_nums)


# --------------------- version 2 --------------------------- judge 100%


lst_1 = list(map(int, input().split(', ')))

for i in lst_1:
    if i == 0:
        lst_1.remove(i)
        lst_1.append(0)

print(lst_1)


""" _______________ Zeros To Back __________________


Write a program that receives a single string (integers separated by a comma and space ", "),
finds all the zeros, and moves them to the back without messing up the other elements.

Print the resulting integer list.


_____________ Test Data _____________


Input 1:
--------
1, 0, 1, 2, 0, 1, 3


Output 1:
---------
[1, 1, 2, 1, 3, 0, 0]


-------------------------------------


Input 2:
-------
0, 5, 0, 4, 0, 0, 5


Output 2:
--------
[5, 4, 5, 0, 0, 0, 0]


-------------------------------------
"""
