# 20220713 - Python Code - Dictionaries - Lecture
# 07 - Word Synonyms - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#6


# ----- version 1 ----- using 'string' as 'value' container ----- judge: 100%


n = int(input())
dct_1 = {}

for i in range(n):
    word = input()
    synonym = input()

    if word not in dct_1.keys():
        dct_1[word] = f'{synonym}'
    else:
        dct_1[word] += f', {synonym}'

for j, k in dct_1.items():
    print(j, '-', k)


# ----- version 2 ----- using 'list' as 'value' container ----- judge: 100%


n = int(input())
dct_1 = {}

for _ in range(n):
    word, synonym = input(), input()

    if word not in dct_1.keys():
        dct_1[word] = [synonym]
    else:
        dct_1[word] += [synonym]

for key, value in dct_1.items():
    print(key, '-', ', '.join(value))
