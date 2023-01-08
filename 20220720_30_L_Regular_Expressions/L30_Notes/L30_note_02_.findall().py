# 20220722 - Python Code - Regular Expressions - Lecture
# Note 02 - .findall()

# use the link to construct the regex: https://regex101.com/

import re


txt = 'The rain in Spain'
x = re.findall('ai', txt)

print(x)                                            # ['ai', 'ai']     - ordered in the order found
