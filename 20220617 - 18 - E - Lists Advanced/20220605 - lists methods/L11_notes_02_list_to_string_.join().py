# 20220601 - Python Code - L11 - Lists Basics
# Notes 020


# ------------------------- .join() ---------------------------
print('\n ----- ex. 1 ----- .join() ----- list => str -----\n')


lst_10 = ['Garry', 'Eric', 'Bill']

str_from_list_10 = (', '.join(lst_10))

print(str_from_list_10)                    # the string from the list
print(lst_10)                              # original list 'lst' still exist


# ------------------------ .join() --------------------------
print('\n----- ex. 2 ----- .join() ----- str => str -----\n')


str_20 = 'First Name'
str_21 = 'Last Name'

str_joined = '-'.join(str_20)
print(str_joined)

str_joined = '-'.join(str_20) + '-'.join(str_21)
print(str_joined)


# ------------------------ creating a list from range and joining it into a string --------
print('\n----- ex. 3 ----- creating a list from range and joining it into a string -----\n')


lst_30 = [n for n in range(1, 11)]

print(lst_30)
print(type(lst_30))
print(type(lst_30[0]))
print()

str_31 = ', '.join(str(lst_30[i]) for i in range(len(lst_30)))      # converts elements of 'lst_31' to 'str' and '.join()' them to 'str'

print(str_31)
print(type(str_31))
print(type(str_31[0]))
