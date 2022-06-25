# 20220528 - Python - Python Fundamentals - L6 - Basic Syntax, Conditional Statements, Loops
# More Exercise 03 - Wolf in Sheep's Clothing - judge url: https://judge.softuni.org/Contests/Practice/Index/1720#2

lst_1 = input().split(', ')
index_wolf = ''

for i in range(len(lst_1)):
    if lst_1[i] == 'wolf':
        index_wolf = i

if index_wolf == (len(lst_1) - 1):
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {len(lst_1) - index_wolf - 1}! You are about to be eaten by a wolf!')
