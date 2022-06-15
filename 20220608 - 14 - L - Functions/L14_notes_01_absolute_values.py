# 20220608 - Python Code - Functions - Lecture
# notes - 01 - Print Absolute Values in a List

# ----------- my version -----------------

str_in = input().split()
lst_out = [abs(float(i)) for i in str_in]
print(lst_out)

# ----------- lecture --------------------

list_of_strings = input().split()

list_of_numbers = []
for n in list_of_strings:
    number = float(n)
    list_of_numbers.append(number)

list_of_absolute_numbers = []
for n in list_of_numbers:
    absolute_number = abs(n)
    list_of_absolute_numbers.append(absolute_number)

print(list_of_absolute_numbers)
