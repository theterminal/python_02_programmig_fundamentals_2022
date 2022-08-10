# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 05 - Print Part Of The ASCII Table - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#4


# ------------- version 2 -------------------- judge 100%


index_start = int(input())
index_end = int(input())
result = ''

for i in range(index_start, index_end + 1):
    char = chr(i)
    result += char + " "

print(result.strip())                           # .strip() takes out the white space from both sides of the string


# ------------- version 1 -------------------- judge 100%


index_start = int(input())
index_end = int(input())
result = ''

for i in range(index_start, index_end + 1):
    char = chr(i)
    if i == index_end:
        result += char
        break
    result += char + " "

print(result)


# ------------- version 3 -------------------- judge 100%


index_start = int(input())
index_end = int(input())
result = ''

for i in range(index_start, index_end + 1):
    if i == index_end:
        result += chr(i)
        break
    result += chr(i) + " "

print(result)


""" ----------------- Print Part Of The ASCII Table --------------------


Write a program that prints part of the ASCII table characters on the console, separated by a single space.
    •	On the first line of input, you will receive the char index you should start with.
    •	On the second line - the index of the last character you should print.


----------- Test Data -----------


Input 1:
-------
60
65


Output 1:
--------
< = > ? @ A


---------------------------------


Input 2:
-------
69
79


Output 2:
--------
E F G H I J K L M N O


---------------------------------


Input 3:
-------
97
104


Output 3:
--------
a b c d e f g h


---------------------------------


Input 4:
-------
40
55


Output 4:
--------
( ) * + , - . / 0 1 2 3 4 5 6 7


--------------------------------

"""
