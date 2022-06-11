# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 04 - Sum of Chars - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#3

# --------- version 1 ---------------------

num_chars = int(input())
sum_of_ascii = 0

for i in range(num_chars):
    number = ord(input())
    sum_of_ascii += number

print(f'The sum equals: {sum_of_ascii}')

# ---------- version 2 --------------------

num_chars = range(int(input()))
sum_of_ascii = 0

for _ in num_chars:
    number = ord(input())
    sum_of_ascii += number

print(f'The sum equals: {sum_of_ascii}')
