# 20220712 - Python - Dictionaries - Lecture
# Notes 07


# --------------------- Lists --------------------------
print('\n--------------------- Lists --------------------------\n')


a = [1, 2, 3]
b = [4, 5, 6]

c = a + b
print(c)                                # result: [1, 2, 3, 4, 5, 6]

d = [*a, *b]
print(d)                                # result: [1, 2, 3, 4, 5, 6]

d = [*a, *b, *a]
print(d)                                # result: [1, 2, 3, 4, 5, 6, 1, 2, 3]


# --------------------- Dictionaries --------------------------
print('\n--------------------- Dictionaries --------------------------\n')


dict_a = {'a1': 1, 'a2': 2}
dict_b = {'b1': 10, 'b2': 20}

dict_d1 = [*dict_a, *dict_b]
print(dict_d1)                          # result: ['a1', 'a2', 'b1', 'b2']

dict_d2 = {*dict_a, *dict_b}
print(dict_d2)                          # result: {'a1', 'b1', 'b2', 'a2'}

dict_d3 = {**dict_a, **dict_b}
print(dict_d3)                          # result: {'a1': 1, 'a2': 2, 'b1': 10, 'b2': 20}
