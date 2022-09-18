# 20220712 - Python - Dictionaries - Lecture
# Notes 14


print('\n\n--------------------------------------------------------\n\n')


dict_1 = {
    'food': {
        'nuts': 'almonds',
        'vegetables': 'tomatoes',
        'fruits': 'apples'
    },
    'drinks': {
        'non-alcoholic': 'water',
        'alcoholic': 'beer'
    }
}

print(dict_1)


print('\n\n--------------------------------------------------------\n\n')


for key_1, value_1 in dict_1.items():
    print(key_1, value_1)


print('\n\n--------------------------------------------------------\n\n')


for key_1, value_1 in dict_1.items():
    for key_2, value_2 in value_1.items():
        print(f'{key_2} - {value_2}')


print('\n\n--------------------------------------------------------\n\n')


for key_1, value_1 in dict_1.items():
    for key_2, value_2 in value_1.items():
        print(value_2)
