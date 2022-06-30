# 20220608


while True:
    num_elements = int(input('\nEnter the number of all elements: '))
    num_elements_in_group = int(input('Enter number of elements in a group: '))

    if num_elements <= 0:
        print(f'Enter a positive \'int\' number!')
    else:
        break

all_permutations = 1
count_cycles = 0
all_permutations_from_group = 0
factorial = 1

for j in range(num_elements, 0, -1):
    all_permutations *= j
    count_cycles += 1
    if count_cycles == num_elements_in_group:
        all_permutations_from_group = all_permutations

for i in range(1, num_elements_in_group + 1):
    factorial *= i

all_combinations_from_group = int(all_permutations_from_group / factorial)

print(f'\nAll permutations from {num_elements} elements (\'{num_elements}!\' - factorial) are: {all_permutations}')
print(f'All variations from {num_elements} elements in groups of {num_elements_in_group} elem. are: {all_permutations_from_group}')
print(f'All combinations from {num_elements} elements in groups of {num_elements_in_group} elem. are: {all_combinations_from_group}')
