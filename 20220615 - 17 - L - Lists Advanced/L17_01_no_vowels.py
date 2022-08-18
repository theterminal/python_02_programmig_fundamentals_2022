# 20220616 - Python - Lists Advance - Lecture
# 01 - No Vowels - judge: https://judge.softuni.org/Contests/Practice/Index/1730#0


# ----------------- version 1 ------------------- judge 100%


str_in = input()

nots = ['a', 'o', 'u', 'e', 'i']
result = [i for i in str_in if i.lower() not in nots]

print(''.join(result))


""" _____________ No Vowels ______________


Using comprehension, write a program that receives a text and removes all its vowels, case insensitive.
Print the new text string after removing the vowels.
The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.


___________ Test Data _______________


Input 1:
-------
Python


Output 1:
--------
Pythn


------------------------------------


Input 2:
-------
ILovePython


Output 2:
--------
LvPythn


-----------------------------------
"""
