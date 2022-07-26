# 20220721 - Python Code - String Processing - Exercise
# More Exercise 02 - ASCII Sumator - judge url: https://judge.softuni.org/Contests/Practice/Index/1741#1


# ---------------------- version 1 ----------------------------- judge: 100%


range_start = ord(input())
range_end = ord(input())
data_in = input()
sum_ascii = 0

for s in data_in:
    if range_start < ord(s) < range_end:
        sum_ascii += ord(s)

print(sum_ascii)
