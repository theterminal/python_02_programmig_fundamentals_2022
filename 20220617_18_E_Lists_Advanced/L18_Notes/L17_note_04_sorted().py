# 20220617 - Python - Lists Advance - Lecture
# Notes - 04 - sorted(), .sort()


"""

sorted() - creates new list from the given!
.sort() - modifies the existing list!

sorts by the length of the words

"""


print('\n\n----- ex. 1 ------ sorted(list, key) -----------------\n\n')


lst_10 = ['three', 'one', 'eleven', 'two', 'eight', 'five']

print(lst_10)                                                      # ['three', 'one', 'eleven', 'two', 'eight', 'five']
print(sorted(lst_10, key=len))                                     # ['one', 'two', 'five', 'three', 'eight', 'eleven']


print('\n\n----- ex. 2 ------ sorted(list, key) with applying functon to the list ------------\n\n')


"""

*) sorted() - sorts on first positions the nums that are 'True' to the function applied

In the example bellow sorted() returned:
the even numbers first (the key is a function that returns 'True' if element is even and 'False' if it is non),
the odd numbers next,
while maintaining the original order.

"""


lst_20 = [3, 4, 1, 8, 5, 6, 9, 2, 7]
print(lst_20)                                                      # [3, 4, 1, 8, 5, 6, 9, 2, 7]


def even_nums(x):
    return x % 2                                                   # returns 'True' or 'False'


sorted_lst_20 = sorted(lst_20, key=even_nums)
print(sorted_lst_20)                                               # [4, 8, 6, 2, 3, 1, 5, 9, 7]


print('\n\n----- ex. 3 ------ sorted(list, key) with applying functon to the list ------------\n\n')


# sorted() - sorts the list in 'reverse' order by value (not index)


lst_30 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst_30)                                                      # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def even_nums(x):
    return x % 2


lst_31 = sorted(lst_30, key=even_nums)

print(lst_31)                                                      # [2, 4, 6, 8, 1, 3, 5, 7, 9]
print(sorted(lst_31, reverse=True))                                # [9, 8, 7, 6, 5, 4, 3, 2, 1]
