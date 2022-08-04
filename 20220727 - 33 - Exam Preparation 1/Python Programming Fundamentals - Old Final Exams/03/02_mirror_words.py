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


""" ----------------- Mirror Words --------------------


The SoftUni Spelling Bee competition is here.
But it`s not like any other Spelling Bee competition out there.
It`s different and a lot more fun!
You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!

On the first line of the input, you will be given a text string.
To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.

First of all, you have to extract the hidden word pairs.

Hidden word pairs are:
    •	Surrounded by "@" or "#" (only one of the two) in the following pattern

#wordOne##wordTwo# or @wordOne@@wordTwo@

    •	At least 3 characters long each (without the surrounding symbols)
    •	Made up of letters only

If the second word, spelled backward, is the same as the first word and vice versa (casing matters!),
they are a match, and you have to store them somewhere.

Examples of mirror words:

#Part##traP# @leveL@@Level@ #sAw##wAs#

    •	If you don`t find any valid pairs, print: "No word pairs found!"
    •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
    •	If there are no mirror words, print: "No mirror words!"
    •	If there are mirror words print:
    
"The mirror words are:
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"


Input / Constraints:
-------------------
    •	You will recive a string.


Output:
------
    •	Print the proper output messages in the proper cases as described in the problem description.
    •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
    •	Each pair of mirror word must be printed with " <=> " between the words.


--------------- Test Data --------------------

Input 1:
-------
@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r


Output 1:
--------
5 word pairs found!
The mirror words are:
Part <=> traP, leveL <=> Level, sAw <=> wAs


----------------------------------------------


Input 2:
-------
#po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@


Output 2:
--------
2 word pairs found!
No mirror words!


-----------------------------------------------


Input 3:
-------
#lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#


Output 3:
--------
No word pairs found!
No mirror words!


-----------------------------------------------

"""
