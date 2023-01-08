# 20220714 - Python - String Processing - Lecture
# Note 01 - str(), .split()


# ---------------- str() ---------------------------


x = 3.5
print(type(x))

str_x = str(x)
print(type(str_x))


# ---------------- split() -------------------------


txt = 'Hello, my name is, Peter'
print(txt)

lst = txt.split(', ')
print(lst)
