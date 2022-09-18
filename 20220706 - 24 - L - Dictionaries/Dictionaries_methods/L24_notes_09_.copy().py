# 20220712 - Python - Dictionaries - Lecture
# Notes 09


# ------------ .copy() ----------------------


dict_1 = {
    'one': 1,
    'two': 2,
    'three': 3
}
print(dict_1)                               # result: {'one': 1, 'two': 2, 'three': 3}

dict_2 = dict_1.copy()
print(dict_2)                               # result: {'one': 1, 'two': 2, 'three': 3}

dict_1['one'] = 100
dict_2['one'] = 1000
print(dict_1)                               # result: {'one': 100, 'two': 2, 'three': 3}
print(dict_2)                               # result: {'one': 1000, 'two': 2, 'three': 3}
