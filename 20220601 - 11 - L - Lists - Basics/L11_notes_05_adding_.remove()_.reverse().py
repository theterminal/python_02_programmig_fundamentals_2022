# 20220604 - Python Code - L11 - Lists Basics
# Notes 04 - Adding elements, .remove(), .reverse()


# --------------- adding element to a list NOT with append --------
print('\nAdding element to a list NOT with append')

lst_1 = ['a', 'b', 'c']
print(lst_1)

for i in range(ord('d'), ord('z') + 1):
    lst_1 += [chr(i)]
print(lst_1)


# --------------- removing elements from a list -------------------
print('\nRemoving elements from a list')

lst_1 = ['a', 'b', 'c']
lst_1.remove('b')
print(lst_1)


# --------------- reversing elements in a list -------------------
print('\nReversing the elements of a list')

lst_1 = ['a', 'b', 'c']
lst_1.reverse()
print(lst_1)
