# 20220608 - Python Code - Functions - Lecture
# 01 - Absolute Values - judge url: https://judge.softuni.org/Contests/Practice/Index/1727#0


# ---------------- no function ---------------------- judge 100%


str_entered = input().split()
lst_from_str_entered_to_abs_num = [abs(float(i)) for i in str_entered]

print(lst_from_str_entered_to_abs_num)


# ---------------- with function -------------------- judge 100%


def absolute(nums):
    return [abs(i) for i in nums]


nums_entered = list(map(float, input().split(' ')))
print(absolute(nums_entered))


""" __________ Absolute Values ___________



Write a program that receives a sequence of numbers,
separated by a single space, and prints their absolute value as a list.
Use abs().


_________ Test Data ___________


Input 1:
-------
1 2.5 -3 -4.5


Output 1:
--------
[1.0, 2.5, 3.0, 4.5]


-------------------------------


Input 2:
-------
-0 1 10 -6.66


Output 2:
--------
[0.0, 1.0, 10.0, 6.66]


-------------------------------
"""
