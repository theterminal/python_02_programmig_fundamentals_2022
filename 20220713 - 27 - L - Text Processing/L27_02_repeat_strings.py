# 20220714 - Python - String Processing - Lecture
# 02 - Repeat Strings - judge url: https://judge.softuni.org/Contests/Practice/Index/1739#1


# --------- version 3 -------------- judge: 100%


def repeat_word(word):
    return word * len(word)


words: list = input().split(' ')
print(''.join(map(repeat_word, words)))


# --------- version 2 -------------- judge: 100%


print(''.join([i * len(i) for i in input().split(' ')]))


# --------- version 1 -------------- judge: 100%


str_in = input().split(' ')
str_out = ''

for s in str_in:
    str_out += (s * len(s))

print(str_out)
