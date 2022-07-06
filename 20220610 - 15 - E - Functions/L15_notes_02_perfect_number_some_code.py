# 20220615 - Python Code - Functions - Exercise
# Notes - Perfect Number


# Start the code and enter integer value for the 'max_num' variable! That is the max of the range...

max_num = int(input())
counter_perfect_numbers = counter_combinations = 0

for num in range(1, max_num + 1):
    while True:
        counter_combinations += 1
        if counter_combinations % 1000 == 0:
            print(f'{counter_combinations} - combination')

        sum_divisors = 0

        for i in range(1, int(num / 2) + 1):
            if num % i == 0:
                sum_divisors += i

        if num == sum_divisors:
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
            print(f'{num} is a perfect number. The sum of its positive divisors equals to the {num} itself!\n')
            counter_perfect_numbers += 1

        break

print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
print(f'{counter_perfect_numbers} - is the count of all perfect numbers in the range (0, {max_num}]\n')
print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
