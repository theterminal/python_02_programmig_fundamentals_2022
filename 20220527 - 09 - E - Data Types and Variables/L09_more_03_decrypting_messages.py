# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 03 - Decrypting Messages - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#2


# --------- version 1 --------------------- judge 100%


key = int(input())
num_lines = range(int(input()))
str_to_print = ''

for _ in num_lines:
    str_to_print += chr(ord(input()) + key)

print(str_to_print)


""" ---------------- Decrypting Messages -----------------


On the first line, you will receive a key (integer).
On the second line, you will receive 'n' – the number of lines, which will follow.
On the next 'n' lines – you will receive a lower and an uppercase letter per line.

You should add the key to each of the characters and append them to a message.
In the end, print the decrypted message.


----------------- Test Data -------------------


Input 1:
-------
3
7
P
l
c
q
R
k
f


Output 1:
--------
SoftUni


-----------------------------------------------


Input 2:
-------
1
7
C
d
b
q
x
o
s


Output 2:
--------
Decrypt


-----------------------------------------------

"""
