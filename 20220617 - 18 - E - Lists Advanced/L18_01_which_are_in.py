# 20220617 - Python - Lists Advance - Exercise
# 01 - Which Are In - judge: https://judge.softuni.org/Contests/Compete/Index/1731#0


# ----------------------------- version 1 ------------------------- judge 100%


lst_1 = input().split(', ')
lst_2 = input().split(', ')

result = []

for i in lst_1:
    for j in range(len(lst_2)):
        if i in lst_2[j]:
            result.append(i)
            break

print(result)


# ----------------------------- version 2 ------------------------- judge 100%


lst_1 = input().split(', ')
lst_2 = input().split(', ')

result = []

for i in lst_1:
    for j in lst_2:
        if i in j:
            result.append(i)
            break

print(result)


""" _______________ Which Are In _______________


You will be given two sequences of strings, separated by ", ".
Print a new list containing only the strings from the first input line,
which are substrings of any string in the second input line.


_______ Test Data ________


Input 1:
-------
arp, live, strong
lively, alive, harp, sharp, armstrong


Output 1:
--------
['arp', 'live', 'strong']


-------------------------


Input 2:
-------
tarp, mice, bull
lively, alive, harp, sharp, armstrong


Output 2:
--------
[]


-------------------------
"""
