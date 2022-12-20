# 20220722 - Python Code - Regular Expressions - Lecture
# 03 - Match Dates - judge url: https://judge.softuni.org/Contests/Practice/Index/1742#2

# use the link to construct the regex: https://regex101.com/

import re


# ------------------------ version 1 -------------------- judge: 100%


dates = input()
regex = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'                  # '\2' means: match the found separator from group 2 for this group also!

result = re.findall(regex, dates)

for match in result:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')
