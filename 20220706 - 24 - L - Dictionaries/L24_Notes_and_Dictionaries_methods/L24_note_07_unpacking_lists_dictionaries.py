# 20220712 - Python - Dictionaries - Lecture
# Note 07 - Unpacking lists and dictionaries


print('\n--------------------- Lists --------------------------\n')


a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)                                # [1, 2, 3, 4, 5, 6]

d = [*a, *b]
print(d)                                # [1, 2, 3, 4, 5, 6]

d = [*a, *b, *a]
print(d)                                # [1, 2, 3, 4, 5, 6, 1, 2, 3]


print('\n--------------------- Dictionaries --------------------------\n')


dict_a = {'key_a1': 1, 'key_a2': 2}
dict_b = {'key_b1': 10, 'key_b2': 20}

dict_d1 = [*dict_a, *dict_b]
print(dict_d1)                          # ['key_a1', 'key_a2', 'key_b1', 'key_b2']

dict_d2 = {*dict_a, *dict_b}
print(dict_d2)                          # {'key_b1', 'key_a1', 'key_b2', 'key_a2'}

dict_d3 = {**dict_a, **dict_b}
print(dict_d3)                          # {'key_a1': 1, 'key_a2': 2, 'key_b1': 10, 'key_b2': 20}
