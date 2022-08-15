# 20220603 - Python - L12 - Lists Basics - Exercise
# 04 - Number Beggars - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#3


# ---------------------- version 1 --------------------------------- judge 100%


lst_nums = list(map(int, input().split(', ')))
num_beggars = int(input())

lst_out = []

for beggar in range(num_beggars):
    sum_current_beggar = 0

    for num in range(beggar, len(lst_nums), num_beggars):
        sum_current_beggar += lst_nums[num]

    lst_out.append(sum_current_beggar)

print(lst_out)


# ---------------------- version 2 --------------------------------- judge 100%


lst_collect = list(map(int, input().split(', ')))
num_collectors = int(input())

lst_collector_final = []

for collector in range(num_collectors):
    middle_list = lst_collect[collector::num_collectors]
    lst_collector_final.append(sum(middle_list))

print(lst_collector_final)


""" __________________ Number Baggers ____________________


You will receive 2 lines of input.
    •	On the first line, you will receive a single string of integers, separated by a comma and a space ", ".
    •	On the second line, you will receive a count of beggars.

Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns,
from the first to the last number in the list.

For example:    [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6,
                as the first one takes [1, 3, 5],
                the second one collects [2, 4].
                
                The same list with 3 beggars would produce a better outcome for the second beggar:
                5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
                
Also, note that not all beggars have to take the same amount of "offers",
meaning that the length of the list is not necessarily a multiple of 'n'.
The list length could be even shorter - i.e., the last beggars will take nothing (0).


_____________ Test Data _______________


Input 1:
-------
1, 2, 3, 4, 5
2


Output 1:
--------
[9, 6]


---------------------------------------


Input 2:
-------
3, 4, 5, 1, 29, 4
6


Output 2:
--------
[3, 4, 5, 1, 29, 4]


---------------------------------------


Input 3:
-------
100, 94, 24, 99
5


Output 3:
--------
[100, 94, 24, 99, 0]


---------------------------------------
"""
