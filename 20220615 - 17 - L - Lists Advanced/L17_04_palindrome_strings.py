# 20220617 - Python - Lists Advance - Lecture
# 04 - Palindrome Strings - judge: https://judge.softuni.org/Contests/Practice/Index/1730#3


# ----------------- version 1 ------------------------- judge 100%


words_in = input().split(' ')
palindrome_in = input()
palindrome_out = []

for i in words_in:
    if i[:int(int(len(i)) / 2)] == i[-1: int(len(i) / 2):-1]:           # if i == i[::-1] - it is a palindrome
        palindrome_out.append(i)

number = 0
if palindrome_in in palindrome_out:
    number = palindrome_out.count(palindrome_in)

print(palindrome_out)
print(f'Found palindrome {number} times')


# ----------------- version 2 ------------------------- judge 100%


def palindrome_filter(x):
    if x == x[::-1]:
        return x


words = input().split(' ')
palindrome = input()

palindrome_list = [word for word in words if palindrome_filter(word)]
print(palindrome_list)
print(f'Found palindrome {palindrome_list.count(palindrome)} times')


""" _______________ Palindrome Strings _______________


On the first line, you will receive words separated by a single space.
On the second line, you will receive a palindrome.

First, you should print a list containing all the found palindromes in the sequence.
Then, you should print the number of occurrences of the given palindrome in the format:
"Found palindrome {number} times".


__________ Test Data ____________


Input 1:
-------
wow father mom wow shirt stats
wow


Output 1:
--------
['wow', 'mom', 'wow', 'stats']
Found palindrome 2 times


---------------------------------


Input 2:
-------
hey how you doin? lol
mom


Output 2:
--------
['lol']
Found palindrome 0 times


--------------------------------
"""
