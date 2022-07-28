# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 02 - Largest of Three Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#1


# ------------------ version 3 ------------------------ judge: 100$


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > num_2:
    if num_1 > num_3:
        print(num_1)
    else:
        print(num_3)
else:
    if num_2 > num_3:
        print(num_2)
    else:
        print(num_3)


# ------------------ version 2 ------------------------ judge: 100$


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 > num_2 and num_1 > num_3:
    print(num_1)
elif num_2 > num_1 and num_2 > num_3:
    print(num_2)
else:
    print(num_3)


# ------------------ version 1 ------------------------ judge: 100$


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

num_largest = max(num_1, num_2, num_3)
print(num_largest)


"""------------------------ Largest of Three Numbers ------------------------


Write a program that receives three whole numbers and prints the largest one.


----------- Examples -----------------


Input 1:
-------
3
-1
5


Output 1:
--------
5


---------------------


Input 2:
-------
0
-1
-2


Output 2:
--------
0


"""