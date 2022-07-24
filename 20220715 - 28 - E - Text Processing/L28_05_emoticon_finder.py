# 20220715 - Python Code - String Processing - Exercise
# 05 - Emoticon Finder - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#4


# ------------------------ version 3 -------------------- judge: 80%


str_in = input()

if ':' in str_in:

    while ':' in str_in:
        index = (str_in.index(':'))

        if index != len(str_in) - 1:
            # if str_in[index + 1] == ':':
            #     str_in = str_in[index + 1:]
            #     continue

            print(str_in[index: index + 2])
            str_in = str_in[index + 2:]

            if len(str_in) <= 1:
                break
        else:
            break


# # ------------------------ version 2 -------------------- judge: 80%
#
#
# str_in = input()
#
# if ':' in str_in:
#     while ':' in str_in:
#         index_1 = (str_in.index(':'))
#         if index_1 != len(str_in) - 1 and str_in[index_1 + 1] != ':':
#             print(str_in[index_1: index_1 + 2])
#             str_in = str_in[index_1 + 2:]
#         else:
#             break
#
#
# # ------------------------ version 1 -------------------- judge: 80%
#
#
# str_in = input()
#
# if ':' in str_in:
#     while ':' in str_in:
#         index_1 = (str_in.index(':'))
#         if index_1 != len(str_in) - 1 and str_in[index_1 + 1] != ' ' and str_in[index_1 + 1] != ':':
#             print(str_in[index_1: index_1 + 2])
#             str_in = str_in[index_1 + 2:]
#         else:
#             break


""" Emoticon Finder

Find all emoticons in the text.
An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.


Example:

---> Input:

There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)

Output: --->

:P
:O
:)

"""