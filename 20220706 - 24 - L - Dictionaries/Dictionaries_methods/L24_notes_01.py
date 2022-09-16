# 20220706 - Python - Dictionaries - Lecture
# Notes - 01


print("\n-------------- creating a dictionary ------------\n")


my_dict = {'name': 'Jack', 'age': 26}                           # {key:value} pairs separated by a ','

print(my_dict)
print(my_dict['name'])                                          # accessing the 'value' of the specified 'key'
print(my_dict['age'])


print("\n-------------- changing keys and values ---------\n")


my_dict['name'] = 'Kiril'                                       # changing the value of the specified key
my_dict['age'] = 48

print(my_dict)
print(my_dict['name'])
print(my_dict['age'])


print("\n---------------------------------------------------\n")


print(f'Printing all the keys of \'my_dict\': ')
for i in my_dict.keys():
    print(i, end=', ')


print("\n\n---------------------------------------------------\n")


print(f'Printing all the values of \'my_dict\': ')
for i in my_dict.values():
    print(i, end=', ')


print("\n\n---------------------------------------------------\n")


print('Printing \'my_dict.items()\' ; \'my_dict.keys()\' ; \'my_dict.values()\' \n')

print(my_dict.items())                                              # result is a list ot tuples
print(my_dict.keys())                                               # result is a list
print(my_dict.values())                                             # result is a list
print(len(my_dict))


print("\n---------------------------------------------------\n")


for i in my_dict:
    print(f'(key:value) pair -> ', i, end=' : ')
    print(my_dict[i])


print("\n---------------------------------------------------\n")


for j, k in my_dict.items():
    print(j, k)


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
