# 20220706 - Python - Dictionaries - Lecture
# Note - 01 - Creating dictionary, changing keys and values


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
