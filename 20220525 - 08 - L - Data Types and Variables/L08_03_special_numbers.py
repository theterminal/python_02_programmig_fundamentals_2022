# 20220529 - Python - Python Fundamentals - L08 - Data Types and Variables
# 03 - Special Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1721#2


# -------------- version 1 --------------- Working with strings ----------- judge: 100%


num_entered = int(input())

for num in range(1, num_entered + 1):
    sum_digits = 0
    str_num = str(num)

    for j in range(len(str_num)):
        num_to_sum = int(str_num[j])
        sum_digits += num_to_sum

    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')


# -------------- version 2 --------------- Working with numbers only ------- judge: 100%


num_entered = int(input())

for num in range(1, num_entered + 1):
    sum_digits = 0
    work_num = num

    while work_num > 0:
        sum_digits += work_num % 10
        work_num = int(work_num / 10)

    if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')


"""------------------ Special Numbers -------------------


Write a program that reads an integer 'n'.
Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False).
A number is special when the sum of its digits is 5, 7, or 11.


----------- Test Data ------------


Input 1:
-------
15


Output 1:
--------
1 -> False
2 -> False
3 -> False
4 -> False
5 -> True
6 -> False
7 -> True
8 -> False
9 -> False
10 -> False
11 -> False
12 -> False
13 -> False
14 -> True
15 -> False


----------------------------------


Input 2:
-------
6


Output 2:
--------
1 -> False
2 -> False
3 -> False
4 -> False
5 -> True
6 -> False


"""
