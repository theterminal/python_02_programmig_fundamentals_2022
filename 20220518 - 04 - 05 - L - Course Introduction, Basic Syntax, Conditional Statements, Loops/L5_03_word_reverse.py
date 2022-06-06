# 20220518 - Python - Python Fundamentals - L5 - Basic Syntax
# 03 - Word Reverse - judge url: https://judge.softuni.org/Contests/Practice/Index/1718#2

# --------------------- version 1 ---------------------------
word = input()
reversed_word = ''

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

# --------------------- version 2 ---------------------------

word_2 = input()
print(word_2[::-1])
