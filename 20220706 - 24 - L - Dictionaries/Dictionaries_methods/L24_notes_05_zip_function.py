# 20220712 - Python - Dictionaries - Lecture
# Notes - 05 - Dictionaries - zip function


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print(f'What is your {q}?  It is {a}.')
