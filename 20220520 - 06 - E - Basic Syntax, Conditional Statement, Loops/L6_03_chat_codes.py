# 20220521 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# 03 - Chat Codes - judge url: https://judge.softuni.org/Contests/Compete/Index/1719#2


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
