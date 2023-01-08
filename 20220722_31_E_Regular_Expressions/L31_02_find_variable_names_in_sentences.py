# 20220722 - Python Code - Regular Expressions - Exercise
# 02 - Find Variable Names In Sentences - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#1

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


sentence = input()
pattern = r'\b_([A-Za-z0-9]+)\b'
matches = re.findall(pattern, sentence)

print(','.join(matches))
