# 20220528 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# More Exercise 04 - Sum of a Beach - judge url: https://judge.softuni.org/Contests/Practice/Index/1720#3


# --------------------------- version 2 ---------------------------------


str_entered = input().lower()
words_to_find = ['sand', 'water', 'fish', 'sun']
num_of_occurrences = 0

for i in range(len(words_to_find)):
    num_of_occurrences += str_entered.count(words_to_find[i])

print(num_of_occurrences)


# --------------------------- version 1 ---------------------------------


str_entered = input().lower()

result = str_entered.count('sand')
result += str_entered.count('water')
result += str_entered.count('fish')
result += str_entered.count('sun')

print(result)
