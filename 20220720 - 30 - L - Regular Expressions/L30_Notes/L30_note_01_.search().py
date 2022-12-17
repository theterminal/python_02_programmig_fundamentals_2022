# 20220722 - Python Code - Regular Expressions - Lecture
# Note 01 - .search()

# use the link to construct the regex: https://regex101.com/

import re


txt = 'The rain in Spain'
x = re.search("^The.*Spain$", txt)
print(x)                                                # <re.Match object; span=(0, 17), match='The rain in Spain'>


# ----------------


string = "The rain in Spain"
x = re.search('\s', string)
print('The first white-space character is located in position:', x.start())
