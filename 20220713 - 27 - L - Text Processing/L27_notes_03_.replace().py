# 20220715 - Python Code - String Processing - Lecture
# 03 - Notes


# ---------------- .replace() ------------------------------------------


txt = 'Windows is not a very good experience!'
txt = txt.replace('W', 'K')
print(txt)

txt = txt.replace('Kindows', '*' * len('Windows'))
print(txt)


print()
# ------------ using the count parameter in the method -----------------


txt = 'apple, apple, apple'
print(txt)

txt = txt.replace('apple', '', 2)
print(txt)

txt = txt.replace(', ', '')
print(txt)


print()
# ------------ when searching in substring -----------------------------


first = 'ice'
second = 'kicegiciceeb'

while first in second:
    second = second.replace(first, '')

print(second)
