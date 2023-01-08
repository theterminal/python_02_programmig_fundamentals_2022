# 20220722 - Python Code - Regular Expressions - Lecture
# 01 - Match Full Name - judge url: https://judge.softuni.org/Contests/Practice/Index/1742#0

# use the link to construct the regex: https://regex101.com/

import re


# ------------------------ version 1 -------------------- judge: 100%


txt = input()

search_for = r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b'
result = re.findall(search_for, txt)
print(' '.join(result))
