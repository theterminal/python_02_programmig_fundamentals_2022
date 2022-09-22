# 20220715 - Python - String Processing - Lecture
# 05 - Digits, Letters and Other - judge url: https://judge.softuni.org/Contests/Practice/Index/1739#4


# ----------------- version 2 ------------------- judge: 100%


def get_digits(data):
    return ''.join([str(ch) for ch in data if ch.isdigit()])


def get_letters(data):
    return ''.join([ch for ch in data if ch.isalpha()])


def get_other(data):
    return ''.join([ch for ch in data if not ch.isdigit() and not ch.isalpha()])


data_in = input()
print(get_digits(data_in))
print(get_letters(data_in))
print(get_other(data_in))


# ----------------- version 1 ------------------- judge: 100%


data_in: str = input()

digits = alpha = other = ''

for symbol in data_in:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        alpha += symbol
    else:
        other += symbol

print(digits)
print(alpha)
print(other)
