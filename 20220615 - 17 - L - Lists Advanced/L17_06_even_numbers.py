# 20220617 - Python - Lists Advance - Lecture
# 06 - Even Numbers - judge: https://judge.softuni.org/Contests/Practice/Index/1730#5


# ----------------- version 1 ------------------- judge 100%


numbers = list(map(int, input().split(', ')))
indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(indices)


""" _____________ Even Numbers ______________


Write a program that reads a single string with numbers separated by comma and space ", ". 
Print the indices of all even numbers.

__________ Test Data ____________


Input 1:
-------
3, 2, 1, 5, 8


Output 1:
--------
[1, 4]


---------------------------------


Input 2:
-------
2, 4, 6, 9, 10


Output 2:
--------
[0, 1, 2, 4]


--------------------------------
"""
