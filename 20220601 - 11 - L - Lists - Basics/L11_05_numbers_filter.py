# 20220601 - Python Code - L11 - Lists Basics
# 05 - Numbers Filter - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#4


# --------------- version 5 ------------------- judge 100%


num_nums = int(input())
result = ''
lst_all_nums = [int(input()) for _ in range(num_nums)]
command = input()

if command == 'even':
    print([i for i in lst_all_nums if i % 2 == 0 or i == 0])
elif command == 'odd':
    print([i for i in lst_all_nums if i % 2 != 0])
elif command == 'negative':
    print([i for i in lst_all_nums if i < 0])
elif command == 'positive':
    print([i for i in lst_all_nums if i >= 0])


# --------------- version 4 ------------------- judge 100%


num_lines = int(input())
lst_to_print = list()

lst_all_nums = [int(input()) for _ in range(num_lines)]         # interesting construct

command = input()

for element in lst_all_nums:

    if command == 'even' and element % 2 == 0:
        lst_to_print.append(element)
        continue

    elif command == 'odd' and element % 2 != 0:
        lst_to_print.append(element)
        continue

    elif command == 'negative' and element < 0: 
        lst_to_print.append(element)
        continue

    elif command == 'positive' and element >= 0:
        lst_to_print.append(element)

print(lst_to_print)


# --------------- version 3 ------------------- judge 100%


num_lines = int(input())
lst_all_nums = list()
lst_to_print = list()

for _ in range(num_lines):
    num_received = int(input())
    lst_all_nums.append(num_received)

command = input()

for element in lst_all_nums:

    if command == 'even' and element % 2 == 0:
        lst_to_print.append(element)
        continue

    elif command == 'odd' and element % 2 != 0:
        lst_to_print.append(element)
        continue

    elif command == 'negative' and element < 0:
        lst_to_print.append(element)
        continue

    elif command == 'positive' and element >= 0:
        lst_to_print.append(element)

print(lst_to_print)


# ------------ version 2 ------------------ judge 100%


num_lines = int(input())
lst_all_nums = list()
lst_to_print = list()
lst_even = []
lst_odd = []
lst_positive = []
lst_negative = []

for _ in range(num_lines):
    num_received = int(input())
    lst_all_nums.append(num_received)
    if num_received % 2 == 0:
        lst_even.append(num_received)
    else:
        lst_odd.append(num_received)

    if num_received >= 0:
        lst_positive.append(num_received)
    else:
        lst_negative.append(num_received)

command = input()

if command == 'even':
    print(lst_even)
elif command == 'odd':
    print(lst_odd)
elif command == 'positive':
    print(lst_positive)
elif command == 'negative':
    print(lst_negative)


# # --------------- version 1 ------------------- judge 100%


num_lines = int(input())
lst_all_nums = list()
lst_to_print = list()

for _ in range(num_lines):
    num_received = int(input())
    lst_all_nums.append(num_received)

command = input()
if command == 'even':
    for i in range(len(lst_all_nums)):
        if lst_all_nums[i] % 2 == 0:
            lst_to_print.append(lst_all_nums[i])

if command == 'odd':
    for i in range(len(lst_all_nums)):
        if lst_all_nums[i] % 2 != 0:
            lst_to_print.append(lst_all_nums[i])

if command == 'negative':
    for i in range(len(lst_all_nums)):
        if lst_all_nums[i] < 0:
            lst_to_print.append(lst_all_nums[i])

if command == 'positive':
    for i in range(len(lst_all_nums)):
        if lst_all_nums[i] >= 0:
            lst_to_print.append(lst_all_nums[i])

print(lst_to_print)


""" --------------- Numbers Filter -----------------


On the first line, you will receive a single number 'n'.
On the following 'n' lines, you will receive integers.

After that, you will be given one of the following commands:
    •	even
    •	odd
    •	negative
    •	positive

Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.


---------- Test Data -----------


Input 1:
-------
5
33
19
-2
18
998
even


Output 1:
--------
[-2, 18, 998]


--------------------------------


Input 2:
-------
3
111
-4
0
negative


Output 2:
--------
[-4]


--------------------------------

"""
