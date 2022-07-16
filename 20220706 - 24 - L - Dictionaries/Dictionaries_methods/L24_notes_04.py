# 20220712 - Python Code - Dictionaries - Lecture
# Notes - 04 - Dictionaries


dict_level_1 = {
    'Jerry': '941-416-2644',                # creating a dictionary with some data
    'Jim': '941-233-6564',
    'Jenn': '941-228-1312'
}

print(dict_level_1)                                     # printing the content of the dictionary

dict_level_1['Kiril'] = '941-264-4222'                   # adding a new 'key:value' pair to the dictionary
print(dict_level_1)

print(list(dict_level_1))                               # prints out a list of all 'keys' in the dictionary
print(sorted(list(dict_level_1)))                       # prints out a sorted list of all 'keys' in the dictionary


dict_level_21 = {'name': 'Ivan_21', 'age': 27}
dict_level_22 = {'name': 'Ivan_22', 'age': 28}
