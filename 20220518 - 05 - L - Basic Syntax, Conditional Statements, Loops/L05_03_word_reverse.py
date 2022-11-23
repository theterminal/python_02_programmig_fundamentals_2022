# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax, Conditional Statements, Loops
# 03 - Word Reverse - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#2


# --------------------- version 2 --------------------------- judge: 100%


word_2 = input()
print(word_2[::-1])


# --------------------- version 1 --------------------------- judge: 100%


word_1 = input()
reversed_word = ''

for i in range(len(word_1) - 1, -1, -1):
    reversed_word += word_1[i]

print(reversed_word)
