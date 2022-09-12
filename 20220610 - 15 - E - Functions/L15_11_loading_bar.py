# 20220615 - Python - Functions - Exercise
# 11 - Loading Bar - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#10


# ---------------------- version 1 -------------------- judge 100%


def loading_bar(num):
    if num == 100:
        return f'{num}% Complete!\n[%%%%%%%%%%]'

    bar_l = int(num / 10) * '%'
    bar_r = (10 - int(num / 10)) * '.'
    bar = bar_l + bar_r
    return f'{num}% [{bar}]\nStill loading...'


int_input_div_10 = int(input())
print(loading_bar(int_input_div_10))


""" ______________ Loading Bar _______________


You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10, 20, 30...).

Your task is to create a function that returns a loading bar depending on the number you have received in the input.
Print the result on the console.

For more clarification, see the examples below.


_____________ Test Data _______________


Input 1:
-------
30


Output 1:
--------
30% [%%%.......]
Still loading...


-----------------------------


Input 2:
-------
50


Output 2:
--------
50% [%%%%%.....]
Still loading...


-----------------------------


Input 3:
-------
100


Output 3:
--------
100% Complete!
[%%%%%%%%%%]


-----------------------------
"""
