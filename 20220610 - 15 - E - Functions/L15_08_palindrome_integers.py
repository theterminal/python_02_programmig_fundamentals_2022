# 20220614 - Python - Functions - Exercise
# 08 - Palindrome Integers - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#7


# ------------- version 3 ---------------------------------------- judge 100% ----------


nums = input().split(', ')

for i in nums:
    if i == i[::-1]:
        print('True')
    else:
        print('False')


# ------------- version 2 ------- function used ------------------ judge 100% ----------


def palindrome(lst_str_nums: list):

    for i in lst_str_nums:
        if len(i) % 2 == 0:
            if i[:int(len(i) // 2)] == i[-1:int(len(i) // 2) - 1: -1]:
                print('True')
            else:
                print('False')

        else:
            if i[:int((len(i) - 1) // 2)] == i[-1: int((len(i) - 1) // 2): -1]:
                print('True')
            else:
                print('False')


str_num_in = input().split(', ')
palindrome(str_num_in)


# ------------- version 1 ------- no function used ------------------ judge 100% ----------


str_num_in = input().split(', ')

for i in str_num_in:
    if len(i) % 2 == 0:
        if i[:int(len(i) // 2)] == i[-1:int(len(i) // 2) - 1: -1]:
            print('True')
        else:
            print('False')

    else:
        if i[:int((len(i) - 1) // 2)] == i[-1: int((len(i) - 1) // 2): -1]:
            print('True')
        else:
            print('False')


""" ____________ Palindrome Integers _____________


A palindrome is a number that reads the same backward as forward, such as 323 or 1001.

Write a function that receives a list of positive integers, separated by comma and space ", ".
The function should check if each integer is a palindrome - True or False.

Print the result.


________ Test Data _________


Input 1:
-------
123, 323, 421, 121


Output 1:
--------
False
True
False
True


----------------------------


Input 2:
-------
32, 2, 232, 1010


Output 2:
--------
False
True
True
False


----------------------------
"""
