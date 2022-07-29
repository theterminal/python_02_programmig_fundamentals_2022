# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 03 - Chat Codes - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#2


# ------------- version 1 ----------------------- judge: 100%


num_messages = int(input())

for _ in range(num_messages):
    code = int(input())

    if code == 88:
        print('Hello')
    elif code == 86:
        print('How are you?')
    elif code < 88 and code != 86:
        print('GREAT!')
    elif code > 88:
        print('Bye.')


""" ---------------- Chat Codes ----------------------


Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes.
He starts by creating a program for only four messages.

Create a program that receives the n number of messages sent.
On the following n lines, it will receive integer numbers.
For each number, the program should print a different message:
•	If the number is 88 - "Hello"
•	If the number is 86 - "How are you?"
•	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
•	If the number is over 88 - "Bye."


------------------ Test Data -------------------------


Input 1:
-------
4
88
86
2
105


Output 1:
--------
Hello
How are you?
GREAT!
Bye.


----------------------------


Input 2:
-------
3
88
88
89


Output 2:
--------
Hello
Hello
Bye.


"""
