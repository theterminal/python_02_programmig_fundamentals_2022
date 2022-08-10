# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 04 - Sum of Chars - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#3


# --------- version 1 --------------------- judge 100%


num_chars = int(input())
sum_of_ascii = 0

for i in range(num_chars):
    number = ord(input())
    sum_of_ascii += number

print(f'The sum equals: {sum_of_ascii}')


# ---------- version 2 -------------------- judge 100%


num_chars = range(int(input()))
sum_of_ascii = 0

for _ in num_chars:
    number = ord(input())
    sum_of_ascii += number

print(f'The sum equals: {sum_of_ascii}')


""" -------------- Sum Of Chars -------------------


Write a program that receives 3 characters.
Concatenate all the characters into one string and print it on the console.


----------- Test Data -------------


Input 1:
-------
a
b
c


Output 1:
--------
abc


-----------------------------------


Input 2:
-------
%
2
o


Output 2:
--------
%2o


----------------------------------


Input 3:
-------
1
5
p


Output 3:
--------
15p


"""
