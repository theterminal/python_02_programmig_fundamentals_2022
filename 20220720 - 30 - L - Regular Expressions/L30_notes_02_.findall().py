# 20220722 - Python Code - Regular Expressions - Lecture
# Notes 02

import re
# use this to construct the regex: https://regex101.com/


# ----------------- .findall() ----------------------


txt = 'The rain in Spain'
x = re.findall('ai', txt)

print(x)                                            # ['ai', 'ai']     - ordered in the order found
