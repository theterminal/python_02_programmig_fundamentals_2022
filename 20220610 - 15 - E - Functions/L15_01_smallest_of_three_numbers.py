# 20220614 - Python Code - Functions - Exercise
# 01 - Smallest of Three Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#0


# --------- version 1 ---------------------------------- judge 100%


def smallest_of_three_numbers(a: int, b: int, c: int):
    result = min(a, b, c)

    return result


p1 = int(input())
p2 = int(input())
p3 = int(input())
print(smallest_of_three_numbers(p1, p2, p3))


# --------- version 2 ---------------------------------- judge 100%


def smallest_of_three_numbers(a: int, b: int, c: int):
    return min(a, b, c)


p1 = int(input())
p2 = int(input())
p3 = int(input())
print(smallest_of_three_numbers(p1, p2, p3))


# --------- version 3 ---------------------------------- judge 100%


def smallest_of_three_numbers(lst_nums):
    return min(lst_nums)


p1 = int(input())
p2 = int(input())
p3 = int(input())

lst_all_nums = [p1, p2, p3]
min_num = smallest_of_three_numbers(lst_all_nums)
print(min_num)


""" _____________ Smallest Of Three Numbers ________________


Write a function that receives three integer numbers and returns the smallest.
Print the result on the console.
Use an appropriate name for the function.


________ Test Data _________


Input 1:
-------
2
5
3


Output 1:
--------
2


----------------------------


Input 2:
-------
600
342
123


Output 2:
--------
123


----------------------------


Input 3:
-------
25
21
4


Output 3:
--------
4


----------------------------
"""
