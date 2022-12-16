# 20220712 - Python - Dictionaries - Lecture
# Note 12 - .setdefault(), .update()


print('\n---------- .setdefault() ----------\n')


dict_1 = {
    'one': 1,
    'two': 2,
    'three': 3
}

print(dict_1)                                    # {'one': 1, 'two': 2, 'three': 3}
print(dict_1.setdefault('default', 3))           # 3
print(dict_1.setdefault('sixteen', 16))          # 16
print(dict_1)                                    # {'one': 1, 'two': 2, 'three': 3, 'default': 3, 'sixteen': 16}


print('\n---------- .update() ----------\n')


dict_2 = {
    'six': 6,
    'seven': 7
}

print(dict_2)                      # {'six': 6, 'seven': 7}

dict_1.update(dict_2)
print(dict_1)                      # {'one': 1, 'two': 2, 'three': 3, 'default': 3, 'sixteen': 16, 'six': 6, 'seven': 7}
