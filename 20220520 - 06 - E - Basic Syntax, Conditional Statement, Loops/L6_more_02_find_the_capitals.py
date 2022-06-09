# 20220525 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# More Exercise 01 - Find The Largest - judge url: https://judge.softuni.org/Contests/Practice/Index/1720#1

str_in = input()
capital_letter_indexes = []

for i in range(len(str_in)):
    if str_in[i].isupper():
        capital_letter_indexes.append(i)

print(capital_letter_indexes)
