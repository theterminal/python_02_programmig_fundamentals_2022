# 20220617 - Python - Lists Advance - Lecture
# Note - 06 - filter()


print('\n\n------ ex. 1 ----- list(filter(lambda x: condition, list_name)----------\n\n')


# Returns a list of even numbers
numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))

print(even_numbers)                                                       # [2, 4, 6]


print('\n\n------ ex. 2 ----- list(map(action, list_name); map(lambda x:); list(filter(lambda x: condition, list_name)----------\n\n')


# Converting the list of strings into a list of numbers
number_list = list(map(int, input().split(", ")))                         # enter 1, 2, 3, 4, 5, 6, 7, 8, 9
print(number_list)

# Find all the even numbers' indices
found_indices_or_no = map(lambda x: x if number_list[x] % 2 == 0 else 'no', range(len(number_list)))
print(found_indices_or_no)                                                # Prints the address of the map object: <map object at 0x10bd77250>

found_indices_or_no = list(found_indices_or_no)
print(found_indices_or_no)                                                # ['no', 1, 'no', 3, 'no', 5, 'no', 7, 'no']

# Filter only the indices
even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))
print(even_indices)                                                       # [1, 3, 5, 7]
