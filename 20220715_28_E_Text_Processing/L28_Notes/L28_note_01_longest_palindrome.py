# 20220719 - Python Code - Lecture - Problem Solving
# 01 - The Longest Palindrome in a String


"""

Find the longest palindrome in a string of symbols

"""


txt = 'abbabbaazzaab'
longest_palindrome = ''

for i in range(len(txt), 1, -1):
    for j in range(0, i):
        if txt[j: i] == ''.join(reversed(txt[j: i])) and len(txt[j: i]) > 1:
            if len(txt[j: i]) > len(longest_palindrome):
                longest_palindrome = txt[j: i]

print(f'The longest palindrome is: \'{longest_palindrome}\' and it contains {len(longest_palindrome)} symbols.')
