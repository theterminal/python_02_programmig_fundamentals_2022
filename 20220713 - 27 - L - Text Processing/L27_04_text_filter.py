# 20220715 - Python - String Processing - Lecture
# 04 - Text Filter - judge url: https://judge.softuni.org/Contests/Practice/Index/1739#3


# ------------------ version 2 ----------------- judge: 100%


banned_words = input().split(', ')
data_in = input()

for word in banned_words:
    if word in data_in:
        data_in = data_in.replace(word, '*' * len(word))

print(data_in)


# ------------------ version 1 ----------------- judge: 100%


banned_words: list = input().split(', ')
text: str = input()

for word in banned_words:
    while word in text:
        text = text.replace(word, '*' * len(word))

print(text)
