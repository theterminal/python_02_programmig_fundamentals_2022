# 20220521 - Python Code
# https://www.youtube.com/watch?v=dlCGc92tAqo&t=4s

# reading several integers as an input, separated by a space

num_1, num_2, num_3 = map(int, input().split(', '))

print(num_1, num_2, num_3)

print(f'The type of num_1 is: {type(num_1)}')

print(f'The type of num_2 is: {type(num_2)}')

print(f'The type of num_3'
      f' is: {type(num_3)}')                                # This syntax is valid!
