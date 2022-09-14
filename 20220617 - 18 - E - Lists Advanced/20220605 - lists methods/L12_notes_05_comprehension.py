# 20220603 - Python - L12 - Lists Basics - Exersice
# Notes 05


# ------------------------ list comprehension -----------------------
print('\n----- ex. 1 ----- list comprehension --------------------\n')


lst_10 = [1, 2, 3, -4, -6]
print(lst_10, '        - original list')

lst_11 = [i * -1 for i in lst_10]                                                # changed the value of elements using list comprehension
print(lst_11, '       - changed the value of elements using list comprehension')
