# 20220722 - Python Code - Regular Expressions - Lecture
# Note 03 - .split()

# use the link to construct the regex: https://regex101.com/

import re


txt = 'The rain in Washington!'
print(re.split('\s', txt))                          # ['The', 'rain', 'in', 'Washington!']
