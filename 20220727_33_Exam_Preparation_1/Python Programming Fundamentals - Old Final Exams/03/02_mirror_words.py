# 20220803 - Python Code - Exam Preparation
# 02 - Mirror Words - judge url: https://judge.softuni.org/Contests/Practice/Index/2307#1

import re


# ------------------------- version 3 ------------------------ judge: 100%


def find_word_pairs(string):
    pattern_1 = r'#([A-Za-z]{3,})##([A-Za-z]{3,})#|@([A-Za-z]{3,})@@([A-Za-z]{3,})@'
    result = re.findall(pattern_1, string)
    temp_list = []

    for tup in result:
        for word in tup:
            if len(word) > 0:
                temp_list.append(word)
    return temp_list


def output(temp_list):
    if len(temp_list) > 0:
        print(f'{int(len(temp_list) / 2)} word pairs found!')
    else:
        print(f'No word pairs found!')

    final_list = []
    for k in range(0, len(temp_list), 2):
        if temp_list[k] == temp_list[k + 1][::-1]:
            final_list.append(temp_list[k])
            final_list.append(temp_list[k + 1])

    if len(final_list) > 0:
        print(f'The mirror words are:')
        result = ''
        for i in range(0, len(final_list), 2):
            if i == len(final_list) - 2:
                result_temp = f'{final_list[i]} <=> {final_list[i + 1]}'
            else:
                result_temp = f'{final_list[i]} <=> {final_list[i + 1]}, '
            result += result_temp
    else:
        result = 'No mirror words!'

    return result


def mirror_words(string):
    pairs = find_word_pairs(string)
    result = output(pairs)
    print(result)


string_in = input()
mirror_words(string_in)


# ------------------------- version 2 ------------------------ judge: 100%


def mirror_words():
    string = input()
    pattern_1 = r'#([A-Za-z]{3,})##([A-Za-z]{3,})#|@([A-Za-z]{3,})@@([A-Za-z]{3,})@'
    result = re.findall(pattern_1, string)

    temp_list = []
    final_list = []

    for tup in result:
        for word in tup:
            if len(word) > 0:
                temp_list.append(word)

    if len(temp_list) > 0:
        print(f'{int(len(temp_list) / 2)} word pairs found!')
    else:
        print(f'No word pairs found!')

    for k in range(0, len(temp_list), 2):
        if temp_list[k] == temp_list[k + 1][::-1]:
            final_list.append(temp_list[k])
            final_list.append(temp_list[k + 1])

    if len(final_list) > 0:
        print(f'The mirror words are:')

        result_3 = ''
        for i in range(0, len(final_list), 2):
            if i == len(final_list) - 2:
                result_2 = f'{final_list[i]} <=> {final_list[i + 1]}'
            else:
                result_2 = f'{final_list[i]} <=> {final_list[i + 1]}, '

            result_3 += result_2
        print(result_3)

    else:
        print('No mirror words!')


mirror_words()


# ------------------------- version 1 ------------------------ judge: 100%


string = input()
pattern_1 = r'#([A-Za-z]{3,})##([A-Za-z]{3,})#|@([A-Za-z]{3,})@@([A-Za-z]{3,})@'
result = re.findall(pattern_1, string)

temp_list = []
final_list = []

for tup in result:
    for word in tup:
        if len(word) > 0:
            temp_list.append(word)

if len(temp_list) > 0:
    print(f'{int(len(temp_list) / 2)} word pairs found!')
else:
    print(f'No word pairs found!')

for k in range(0, len(temp_list), 2):
    if temp_list[k] == temp_list[k + 1][::-1]:
        final_list.append(temp_list[k])
        final_list.append(temp_list[k + 1])

if len(final_list) > 0:
    print(f'The mirror words are:')

    result_3 = ''
    for i in range(0, len(final_list), 2):
        if i == len(final_list) - 2:
            result_2 = f'{final_list[i]} <=> {final_list[i + 1]}'
        else:
            result_2 = f'{final_list[i]} <=> {final_list[i + 1]}, '

        result_3 += result_2
    print(result_3)

else:
    print('No mirror words!')
