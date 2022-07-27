# 20220722 - Python Code - Regular Expressions - Lecture
# 02 - Match Phone Number - judge url: https://judge.softuni.org/Contests/Practice/Index/1742#1

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


search_phone = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
txt = input()
result = re.findall(search_phone, txt)
print(', '.join(result))


# ------------------------ version 2 -------------------- judge: 100%


pattern = r'(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\b'
text = input()
matches = re.findall(pattern, text)
print(", ".join(matches))
