# 20220722 - Python Code - Regular Expressions - Exercise
# 02 - Find Variable Names In Sentences - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#1

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


sentence = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
matches = re.findall(pattern, sentence)

print(','.join(matches))


""" --------------------- Find Variable Names In Sentence ----------------------


Write a program that finds all variable names in each string.
A variable name starts with an underscore ("_") and contains only capital and non-capital letters and digits.
Extract only their names without the underscore.
Try to do this only with regular expressions.
The output consists of all variable names extracted and printed on a single line, separated by a comma.


----------- Examples --------------


Input 1:
-------
The _id and _age variables are both integers.


Output 1:
--------
id,age


-----------------------------------


Input 2:
-------
Calculate the _area of the _perfectRectangle object.


Output 2:
--------
area,perfectRectangle

-----------------------------------


Input 3:
--------
__invalidVariable _evenMoreInvalidVariable_ _validVariable


Output 3:
--------
validVariable


"""