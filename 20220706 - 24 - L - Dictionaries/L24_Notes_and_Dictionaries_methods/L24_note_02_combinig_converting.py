# 20220706 - Python - Dictionaries - Lecture
# Note - 02 - Combining dictionaries, converting lists into dictionaries


print("\n------------ combining dictionaries ---------------\n")


a1 = {'el_1': 1, 'el_2': 2}
a2 = {'el_3': 3, 'el_4': 4}
a = {**a1, **a2}
print(a)


print("\n------------ converting lists into dictionaries ---\n")


lst_1 = ['a', 'b', 'c', 'd']
lst_2 = [1, 2, 3, 4]
print(f'{lst_1}\n{lst_2}\n')

dct_1 = dict(zip(lst_1, lst_2))

print(dct_1)
