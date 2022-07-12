# 20220617 - Python Code - Lists Advance - Lecture
# Notes - 04 - .sorted()


# --------------------------- sorted(list, key) ----------------------
print('\n\n----- ex. 1 ------ sorted(list, key) -----------------\n\n')

# sorted() creates new list from the given! .sort() modifies the existing list!
# sorts by the length of the words


lst_10 = ['three', 'one', 'eleven', 'two', 'eight', 'five']

print(lst_10, '     - original list')
print(sorted(lst_10, key=len), '     - result after sorted(list, key)')       # ['one', 'two', 'five', 'three', 'eight', 'eleven']


# --------------------------- sorted(list, key) with applying functon to the list -----------------
print('\n\n----- ex. 2 ------ sorted(list, key) with applying functon to the list ------------\n\n')


# sorts on first positions the nums that are 'True' to the function applied


lst_20 = [3, 4, 1, 8, 5, 6, 9, 2, 7]
print(lst_20, '- original list')


def even_nums(x):
    return x % 2                                # this line returns 'True' or 'False'


sorted_lst_20 = sorted(lst_20, key=even_nums)
print(sorted_lst_20, '- returned the even numbers first, then the odd numbers and maintainded the original order')


# --------------------------- sorted(list, key) with applying functon to the lis -----------------
print('\n\n----- ex. 3 ------ sorted(list, key) with applying functon to the list ------------\n\n')


# sorts the list in 'reverse' order


lst_30 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst_30, '     - original list')


def even_nums(x):
    return x % 2


lst_31 = sorted(lst_30, key=even_nums)

print(lst_31, '     - sorted with key and function')                           # [2, 4, 6, 8, 1, 3, 5, 7, 9]
print(sorted(lst_31, reverse=True), '     - sorted with \'reverse=True\'')     # [9, 8, 7, 6, 5, 4, 3, 2, 1] - !!! reverses back by the value not by index !!!

