# 20220712 - Python - Dictionaries - Lecture
# Note 10 - .pop() and .popitem()


# ------------ .pop() ----------------------


dict_1 = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}
print(dict_1)

print(dict_1.pop('two'))                    # it deletes the pair with the specified key and returns the key
print(dict_1)


# ------------ .popitem() ----------------------


print(dict_1.popitem())
print(dict_1)


# ------------ del ----------------------


del dict_1['three']
print(dict_1)

del dict_1
print(dict_1)                               # it returns 'undefined' because del deletes the dictionary
