# 20220525 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# More Exercise 02 - Find The Capitals - judge url: https://judge.softuni.org/Contests/Practice/Index/1720#1


# ------------------------ version 2 ------- list comprehension ---------------- judge: 100%


str_in = input()
print([i for i in range(len(str_in)) if str_in[i].isupper()])


# ------------------------ version 1 ------------------------------------------- judge: 100%


str_in = input()
capital_letter_indexes = []

for i in range(len(str_in)):
    if str_in[i].isupper():
        capital_letter_indexes.append(i)

print(capital_letter_indexes)
