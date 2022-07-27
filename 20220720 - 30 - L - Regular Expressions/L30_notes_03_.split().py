# 20220722 - Python Code - Regular Expressions - Lecture
# Notes

import re
# use this to construct the regex: https://regex101.com/


# ----------------- .split() ----------------------


txt = 'The rain in Washington!'
print(re.split('\s', txt))                          # ['The', 'rain', 'in', 'Washington!']
