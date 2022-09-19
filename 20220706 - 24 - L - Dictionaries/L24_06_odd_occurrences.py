# 20220713 - Python - Dictionaries - Lecture
# 06 - Odd Occurrences - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#5


# ------------ version 04 ------------------------- judge: 100%


words = [i.lower() for i in input().split(' ')]
dct_1 = {}

for word in words:
    if word not in dct_1:
        dct_1[word] = 0
    dct_1[word] += 1

for key, value in dct_1.items():
    if value % 2 != 0:
        print(key, end=" ")


# ------------ version 02 ------------------------- judge: 100%


data_in = [i.lower() for i in input().split(' ')]
result = []
[result.append(word) for word in data_in if data_in.count(word) % 2 != 0 and word not in result]
print(' '.join(result))


# ------------ version 01 ------------------------- judge: 100%


data_in = [i.lower() for i in input().split(' ')]
result = []

for word in data_in:
    if data_in.count(word) % 2 != 0 and word not in result:
        result.append(word)

print(' '.join(result))


# ------------ version 03 ------------------------- judge: 100%


from collections import defaultdict

words = input().split(' ')
counter_of_words = defaultdict(int)

for word in words:
    counter_of_words[word.lower()] += 1

print(' '.join([word for word, count in counter_of_words.items() if count % 2 != 0]))


# --------------------- example for defaultdict -------------------


from collections import defaultdict

int_dict = defaultdict(int)
float_dict = defaultdict(float)
string_dict = defaultdict(str)

print(int_dict['key - 1'])
print(float_dict['key - 1'])
print(string_dict['key - 1'])

print(int_dict)
print(float_dict)
print(string_dict)
