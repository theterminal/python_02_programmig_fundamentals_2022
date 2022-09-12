# 20220615 - Python - Functions - More Exercise
# 05 - Multiplication Sign - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#4


# -------------- version 2 -------------------------- judge 100%


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

result = [sign(num_1), sign(num_2), sign(num_3)]

if 0 in result:
    print('zero')
elif sum(result) == -1 or sum(result) == 3:
    print('positive')
else:
    print('negative')


# -------------- version 1 -------------------------- judge 100%


def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

final_result = [sign(num_1), sign(num_2), sign(num_3)]

if final_result[0] == 0 or final_result[1] == 0 or final_result[2] == 0:
    print('zero')
elif sum(final_result) == -1 or sum(final_result) == 3:
    print('positive')
else:
    print('negative')


""" -______________ Multiplication Sign ______________


You will receive three integer numbers.
Write a program that finds if their multiplication (the result) is negative, positive, or zero.
Try to do this WITHOUT multiplying the 3 numbers.


___________ Test Data ______________


Input 1:
-------
2
3
-1


Output 1:
--------
negative


-----------------------------------


Input 2:
-------
2
3
1


Output 2:
--------
positive


"""
