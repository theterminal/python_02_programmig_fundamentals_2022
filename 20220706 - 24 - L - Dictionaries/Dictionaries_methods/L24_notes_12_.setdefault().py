# 20220712 - Python - Dictionaries - Lecture
# Notes 12


# ------------ .setdefault() -----------------------------------------------------


dict_1 = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}
print(dict_1)
print(dict_1.setdefault('four', 4))
print(dict_1.setdefault('sixteen', 16))
print(dict_1)


# ------------ .update() ----------------------------------------------------------
print('\n-----------------------------------------------------------------------\n')


dict_2 = {
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}
print(dict_2)

dict_1.update(dict_2)
print(dict_1)
