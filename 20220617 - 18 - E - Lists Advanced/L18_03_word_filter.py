# 20220617 - Python - Lists Advance - Exercise
# 03 - Word Filter - judge: https://judge.softuni.org/Contests/Compete/Index/1731#2


# -------------- version 1 ---------------------------------- judge 100%


lst_text = input().split(' ')

for i in [j for j in lst_text if len(j) % 2 == 0]:
    print(i)


# -------------- version 2 ---------------------------------- judge 100%


for i in [j for j in input().split(' ') if len(j) % 2 == 0]:
    print(i)


# -------------- version 3 ---------------------------------- judge 100%


print('\n'.join([i for i in input().split() if len(i) % 2 == 0]))


""" __________ Word Filter __________


Using comprehension, write a program that receives some text, separated by space,
and take only those words whose length is even.

Print each word on a new line.


_________ Test Data ___________


Input 1:
-------
kiwi orange banana apple


Output 1:
--------
kiwi
orange
banana


-------------------------------


Input 2:
-------
pizza cake pasta chips


Output 2:
--------
cake


------------------------------
"""
