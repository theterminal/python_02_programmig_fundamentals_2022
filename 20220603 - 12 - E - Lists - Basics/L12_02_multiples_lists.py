# 20220603 - Python - L12 - Lists Basics - Exercise
# 02 - Multiple Lists - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#1


# ----------------- version 1 ------------------------------- judge 100%


factor = int(input())
count = int(input())

list_1 = []
counter = 1

for i in range(factor, factor + count):
    num_to_list = counter * factor
    list_1.append(num_to_list)
    counter += 1

print(list_1)


# ----------------- version 2 ------------------------------- judge 100%


factor = int(input())
count = int(input())

list_1 = []

for i in range(1, count + 1):
    list_1.append(factor * i)

print(list_1)


# -------------------- version 3 ----------------------------- judge 100%


factor = int(input())
count = int(input())

print(list(range(factor, count * factor + 1, factor)))


# -------------------- version 4 ----------------------------- judge 100%


factor = int(input())
count = int(input())

print([factor * i for i in range(1, count + 1)])


""" ________________ Multiples Lists __________________


Write a program that receives two numbers (factor and count).
It should create a list with a length of the given count that contains only integer numbers, which are multiples of the given factor.
The numbers should be only positive, and they should be arranged in ascending order, starting from the value of the factor.


______________ Test Data _____________


Input 1:
-------
2
5


Output 1:
--------
[2, 4, 6, 8, 10]


--------------------------------------


Input 2:
-------
1
10


Output 2:
--------
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


--------------------------------------

"""