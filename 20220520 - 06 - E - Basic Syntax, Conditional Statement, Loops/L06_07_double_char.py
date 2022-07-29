# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 07 - Double Char - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#6


# ---------- version 1 ----------------- judge: 100%


while True:
    str_to_test = input()

    if str_to_test == "End":
        break

    if str_to_test == "SoftUni":
        continue

    for j, k in enumerate(str_to_test):
        print(k * 2, end="")
    print()


# ---------- version 2 ----------------- judge: 100%


while True:
    str_in = input()

    if str_in == 'End':
        break

    if str_in == 'SoftUni':
        continue

    for i in str_in:
        print(i * 2, end='')

    print()


''' ------------------ Double Char ------------------


You will be given strings until you receive the command "End".
For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
Note that if you receive the string "SoftUni", you should NOT print it!


----------- Test Data ------------


Input 1:
-------
Hello World
Repeat
End


Output 1:
--------
HHeelllloo  WWoorrlldd
RReeppeeaatt


---------------------------------


Input 2:
-------
1234!
SoftUni
softuni
End


Output 2:
--------
11223344!!
ssooffttuunnii


'''
