# 20220722 - Python Code - Regular Expressions - Lecture
# Notes 01

import re

# use this to construct the regex: https://regex101.com/


# ----------------- .search() ----------------------


txt = 'The rain in Spain'
x = re.search("^The.*Spain$", txt)
print(x)                                                # <re.Match object; span=(0, 17), match='The rain in Spain'>


# ----------------


string = "The rain in Spain"
x = re.search('\s', string)
print('The first white-space character is located in position:', x.start())
