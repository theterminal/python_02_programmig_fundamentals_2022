# 20220722 - Python Code - Regular Expressions - Lecture
# 04 - Match Numbers - judge url: https://judge.softuni.org/Contests/Practice/Index/1742#3

# use the link to construct the regex: https://regex101.com/

import re


# ------------------------ version 1 -------------------- judge: %


numbers = input()

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
result = re.finditer(pattern, numbers)

for match in result:
    print(match.group(), end=' ')
