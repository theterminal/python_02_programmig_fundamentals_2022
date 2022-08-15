# 20220603 - Python - L12 - Lists Basics - Exercise
# 05 - Faro Shuffle - judge url: https://judge.softuni.org/Contests/Compete/Index/1725#4


# ------------------------ version 1 -------------------------- judge 100%


lst_cards_given = input().split(' ')
num_shuffles = int(input())

len_cards_given_dev_2 = int(len(lst_cards_given) / 2)               # can use 'len // 2' and it'll be no problem for int!
lst_cards_to_work_with = lst_cards_given.copy()
lst_to_shuffle = []

while num_shuffles > 0:
    lst_left = lst_cards_to_work_with[:len_cards_given_dev_2]
    lst_right = lst_cards_to_work_with[len_cards_given_dev_2::]

    for i in range(len_cards_given_dev_2):
        lst_to_shuffle.append(lst_left[i])
        lst_to_shuffle.append(lst_right[i])

    lst_cards_to_work_with = lst_to_shuffle.copy()
    lst_to_shuffle.clear()
    num_shuffles -= 1

print(lst_cards_to_work_with)


""" ______________ Faro Shuffle ________________


A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
Then the cards in the two halves are perfectly interleaved,
such that the original bottom card is still on the bottom and the original top card is still on top.

For example, faro shuffling the list
['ace', 'two', 'three', 'four', 'five', 'six'] once, gives
['ace', 'four', 'two', 'five', 'three', 'six']

Write a program that receives a single string (cards separated by space) and
on the second line receives a count of faro shuffles that should be made.

Print the state of the deck after the shuffle.

Note: The length of the deck of cards will always be an even number.


__________________ Test Data ___________________


Input 1:
-------
a b c d e f g h
5


Output 1:
--------
['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']


------------------------------------------------


Input 2:
-------
one two three four
3


Output 2:
--------
['one', 'three', 'two', 'four']


------------------------------------------------
"""
