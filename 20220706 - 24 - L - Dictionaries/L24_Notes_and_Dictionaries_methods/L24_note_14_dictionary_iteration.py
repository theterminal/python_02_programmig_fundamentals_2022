# 20220712 - Python - Dictionaries - Lecture
# Note 14 - Dictionary iteration


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

print(dict_1)                   # {'food': {'nuts': 'almonds', 'vegetables': 'tomatoes', 'fruits': 'apples'}, 'drinks': {'non-alcoholic': 'water', 'alcoholic': 'beer'}}


print('\n\n--------------------------------------------------------\n\n')


for key, value in dict_1.items():
    print(key, value)               # food {'nuts': 'almonds', 'vegetables': 'tomatoes', 'fruits': 'apples'}
#                                   # drinks {'non-alcoholic': 'water', 'alcoholic': 'beer'}


print('\n\n--------------------------------------------------------\n\n')


for k_1, v_1 in dict_1.items():
    for k_2, v_2 in v_1.items():
        print(f'{k_2} - {v_2}')     # nuts - almonds
#                                     vegetables - tomatoes
#                                     fruits - apples
#                                     non-alcoholic - water
#                                     alcoholic - beer

print('\n\n--------------------------------------------------------\n\n')


for k_1, v_1 in dict_1.items():
    for k_2, v_2 in v_1.items():
        print(v_2)                  # almonds
#                                     tomatoes
#                                     apples
#                                     water
#                                     beer
