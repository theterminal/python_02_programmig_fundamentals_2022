# 20220722 - Python Code - Regular Expressions - Exercise
# 04 - Extract Emails - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#3

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%

string = input()

pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
matches = re.findall(pattern, string)
# print(matches[0][0])

for element in matches:
    print(element[0])
