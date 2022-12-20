# 20220722 - Python Code - Regular Expressions - Exercise
# 01 - Capture Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#0

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


pattern = r'\d+'

while True:
    line = input()
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end=' ')
    else:
        break
