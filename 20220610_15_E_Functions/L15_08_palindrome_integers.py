# 20220614 - Python - Functions - Exercise
# 08 - Palindrome Integers - judge url: https://judge.softuni.org/Contests/Compete/Index/1728#7


# ------------- version 3 ---------------------------------------- judge 100% ----------


nums = input().split(', ')

for i in nums:
    if i == i[::-1]:
        print('True')
    else:
        print('False')


# ------------- version 2 ------- function used ------------------ judge 100% ----------


def palindrome(lst_str_nums: list):

    for i in lst_str_nums:
        if len(i) % 2 == 0:
            if i[:int(len(i) // 2)] == i[-1:int(len(i) // 2) - 1: -1]:
                print('True')
            else:
                print('False')

        else:
            if i[:int((len(i) - 1) // 2)] == i[-1: int((len(i) - 1) // 2): -1]:
                print('True')
            else:
                print('False')


str_num_in = input().split(', ')
palindrome(str_num_in)


# ------------- version 1 ------- no function used ------------------ judge 100% ----------


str_num_in = input().split(', ')

for i in str_num_in:
    if len(i) % 2 == 0:
        if i[:int(len(i) // 2)] == i[-1:int(len(i) // 2) - 1: -1]:
            print('True')
        else:
            print('False')

    else:
        if i[:int((len(i) - 1) // 2)] == i[-1: int((len(i) - 1) // 2): -1]:
            print('True')
        else:
            print('False')
