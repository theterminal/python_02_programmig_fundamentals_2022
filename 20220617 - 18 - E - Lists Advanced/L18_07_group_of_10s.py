# 20220617 - Python - Lists Advance - Exercise
# 07 - Group of 10's - judge: https://judge.softuni.org/Contests/Compete/Index/1731#6


# ------------------- version 1 ------------------- judge 100%


lst_in = list(map(int, input().split(', ')))
rng_start = 0
rng_end = 10
lst_out = []
values_to_remove = []

while len(lst_in) > 0:
    for num in lst_in:
        while num in range(rng_start, rng_end + 1):
            lst_out.append(num)
            values_to_remove.append(num)
            break

    print(f'Group of {rng_end}\'s: {lst_out}')
    rng_start += 10
    rng_end += 10
    lst_out.clear()

    for value in values_to_remove:
        lst_in.remove(value)

    values_to_remove.clear()


""" ___________ Group of 10's ____________


Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
and prints the numbers sorted into lists of 10's in the format:

"Group of {group}'s: {list_of_numbers}".

Examples:
    •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
    •	The numbers 13, 19, 14, and 15 fall into the group of 20's.

For more clarification, see the examples below.


_______ Test Data ________


Input 1:
-------
8, 12, 38, 3, 17, 19, 25, 35, 50


Output 1:
--------
Group of 10's: [8, 3]
Group of 20's: [12, 17, 19]
Group of 30's: [25]
Group of 40's: [38, 35]
Group of 50's: [50]


--------------------------


Input 2:
-------
1, 3, 3, 4, 34, 35, 25, 21, 33


Output 2:
--------
Group of 10's: [1, 3, 3, 4]
Group of 20's: []
Group of 30's: [25, 21]
Group of 40's: [34, 35, 33]


---------------------------
"""
