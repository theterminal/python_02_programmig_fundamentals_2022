# 20220601 - Python Code - L11 - Lists Basics
# 04 - Search - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#3

# ------------ version 1 ------------------

num_strings = int(input())
word = input()

lst_strings = []
for _ in range(num_strings):
    str_entered = input()
    lst_strings.append(str_entered)

print(lst_strings)

lst_with_word = []
for i in range(num_strings):
    if word in lst_strings[i]:
        lst_with_word.append(lst_strings[i])

print(lst_with_word)

# ------------ version 2 ------------------

num_strings = int(input())
word = input()

lst_strings = []
lst_with_word = []

for _ in range(num_strings):
    str_entered = input()
    lst_strings.append(str_entered)
    if word in str_entered:
        lst_with_word.append(str_entered)

print(lst_strings)
print(lst_with_word)
