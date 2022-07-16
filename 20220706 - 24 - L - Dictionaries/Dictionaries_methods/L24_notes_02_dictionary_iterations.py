# 20220706 - Python Code - Dictionaries - Lecture
# Notes - 02 - Iterations


my_dict = {
    1: 'one',
    2: 'two',
    3: 'three'
}


print('\n----------------------------- .keys() ----------------------------------\n')


for i in my_dict.keys():
    print(i)


print('\n---------------------------------\n')


for i in my_dict.keys():  # returns the values of the keys
    print(my_dict[i])


print('\n---------------------------------\n')


print(1 in my_dict)  # result shows that 'in' searches only the 'keys' of the dictionary
print('one' in my_dict)  # result shows that 'in' searches only the 'keys' of the dictionary


print('\n----------------------------- .values() ----------------------------------\n')


for i in my_dict.values():
    print(i)


print('\n----------------------------- .items() ----------------------------------\n')


for i in my_dict.items():
    print(i)  # returns tuples


print('\n---------------------------------\n')


for i, j in my_dict.items():
    print(i, j)
