# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 06 - Triples Of Latin Letters - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#5


# --------- version 1 --------------------- judge 100%


num_letters = int(input())
ascii_range = range(97, 97 + num_letters)

for char_1 in ascii_range:
    for char_2 in ascii_range:
        for char_3 in ascii_range:

            print(f'{chr(char_1)}{chr(char_2)}{chr(char_3)}')


""" ----------------- Triples Of Lain Letters --------------------


Write a program to read an integer N and print all triples of the first N small Latin letters, ordered alphabetically:


-------------- Test Data -----------------


Input 1:
-------
3


Output 1:
--------
aaa
aab
aac
aba
abb
abc
aca
acb
acc
baa
bab
bac
bba
bbb
bbc
bca
bcb
bcc
caa
cab
cac
cba
cbb
cbc
cca
ccb
ccc


-----------------------------------------


Input 2:
-------
2


Output 2:
--------
aaa
aab
aba
abb
baa
bab
bba
bbb


-----------------------------------------

"""
