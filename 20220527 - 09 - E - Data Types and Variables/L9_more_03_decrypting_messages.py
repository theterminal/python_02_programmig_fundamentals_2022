# 20220528 - Python - Python Fundamentals - L9 - Data Types and Variables
# More Exercises 03 - Decrypting Messages - judge url: https://judge.softuni.org/Contests/Practice/Index/1723#2


key = int(input())
num_lines = range(int(input()))
str_to_print = ''

for _ in num_lines:
    str_to_print += chr(ord(input()) + key)

print(str_to_print)
