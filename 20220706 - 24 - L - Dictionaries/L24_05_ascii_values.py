# 20220712 - Python - Dictionaries - Lecture
# 05 - ASCII Values - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#4


# ------------------------------- version 1 ------------------ judge: 100%


data_in = input().split(', ')

dict_data_in = {}

for i in data_in:
    dict_data_in[i] = ord(i)

print(dict_data_in)


# ------------------------------- version 2 ------------------ judge: 100%


print({i: ord(i) for i in input().split(', ')})
