# 20220715 - Python - String Processing - Exercise
# 04 - Caesar Cipher - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#3


# ------------------------ version 1 -------------------- judge: 100%


str_in = input()
str_out = ''

for char in str_in:
    str_out += chr(ord(char) + 3)

print(str_out)
