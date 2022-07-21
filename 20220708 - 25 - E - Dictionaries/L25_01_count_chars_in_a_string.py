# 20220713 - Python Code - Dictionaries - Exercise
# 01 - Count Chars In A String - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#0


# ------------- version 2 ------- using string ------------ judge: 100%


data_in = ''.join(s for s in input().split(' '))
dct = {}

for char in data_in:
    if char not in dct.keys():
        dct[char] = 0
    dct[char] += 1

for k, v in dct.items():
    print(f'{k} -> {v}')


# ------------- version 1 -------- using list ----------- judge: 100%


data_in = input().split(' ')
dct = {}

for word in data_in:
    for char in word:
        if char not in dct.keys():
            dct[char] = 0
        dct[char] += 1

for k, v in dct.items():
    print(k, '->', v)
