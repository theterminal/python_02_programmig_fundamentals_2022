# 20220617 - Python - Lists Advance - Lecture
# 05 - Sorting Names - judge: https://judge.softuni.org/Contests/Practice/Index/1730#4


# ----------------- version 1 ------------------- judge 100%


lst_names = input().split(', ')
lst_names_sorted = sorted(lst_names, key=lambda x: (-len(x), x))
print(lst_names_sorted)


""" ______________ Sorting Names _____________


Write a program that reads a single string with names separated by comma and space ", ".
Sort the names by their length in descending order.
If 2 or more names have the same length, sort them in ascending order (alphabetically).
Print the resulting list.


___________ Test Data ______________


Input 1:
-------
Ali, Marry, Kim, Teddy, Monika, John


Output 1:
--------
["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]


------------------------------------


Input 2:
-------
Lilly, Tim, Kate, Tom, Alex


Output 2:
--------
['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']


-----------------------------------
"""
