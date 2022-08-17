# 20220614 - Python Code - Functions - Exercise
# 10 - Perfect Number - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#9


# ----------------- version 1 -------------------- judge 100%


def perfect_number(num_1: int):
    sum_divisors = 0
    for i in range(1, int(num_1 / 2) + 1):
        if num_1 % i == 0:
            sum_divisors += i

    if num_1 == sum_divisors:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


num_to_test = int(input())
perfect_number(num_to_test)


""" ______________ Perfect Number _______________


A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).

Write a function that receives an integer number and returns one of the following messages:
•	"We have a perfect number!" - if the number is perfect.
•	"It's not so perfect." - if the number is NOT perfect.
Print the result on the console.


___________ Test Data ______________


Input 1:
-------
6


Output 1:
--------
We have a perfect number!


------------------------------------


Input 2:
-------
28


Output 2:
--------
We have a perfect number!


------------------------------------


Input 3:
-------
1236498


Output 3:
---------
It's not so perfect.


------------------------------------
"""
