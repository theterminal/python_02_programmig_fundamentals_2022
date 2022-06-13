# 20220601 - Python Code - L11 - Lists Basics
# Notes 01 - String to List conversion, .join(), some list comp-n

# --------- .join() --------------------------------------------

print('\n ----------- .join() ----------------------')
lst = ['Garry', 'Eric', 'Bill']

str_from_list = (', '.join(lst))

print(str_from_list)                    # the string from the list
print(lst)                              # original list 'lst' still exist

# --------- .join() --------------------------------------------

print('\n')

str_1 = 'First Name'
str_2 = 'Last Name'

str_joined = '-'.join(str_1)
print(str_joined)

str_joined = '-'.join(str_1) + '-'.join(str_2)
print(str_joined)

# ------ .join lists into a string ------------------------------

print('\n---------- join lists into a string ------------\n')

lst_1 = ['Firs Name', 'Last Name', 'Age']
lst_joint = ', '.join(lst_1)

print(lst_joint)
print(type(lst_joint))

# ------ creating a list form a range and joining it into a string --------------------------------------

print('\n---------- creating a list form a range and joining it into a string ---------------\n')

lst_1 = [n for n in range(1, 11)]

print(lst_1)
print(type(lst_1))
print(type(lst_1[0]))
print()

str_1 = ', '.join(str(lst_1[i]) for i in range(len(lst_1)))

print(str_1)
print(type(str_1))
print(type(str_1[0]))
