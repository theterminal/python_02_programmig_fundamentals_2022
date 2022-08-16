# 22020624 - Python - L12 - Lists Basics - More Exercise
# 03 - Car Race - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#2


# __________________ version 1 ___________________ judge 100%


nums_line = list(map(int, input().split(' ')))

left_driver = 0
right_driver = 0
driver = ''
winner = ''

length = (len(nums_line) - 1) // 2

for i in range(length):
    if nums_line[i] == 0:
        left_driver *= 0.8
    else:
        left_driver += nums_line[i]

for k in range(len(nums_line) - 1, length, -1):
    if nums_line[k] == 0:
        right_driver *= 0.8
    else:
        right_driver += nums_line[k]

if left_driver < right_driver:
    winner = left_driver
    driver = 'left'

elif right_driver < left_driver:
    winner = right_driver
    driver = 'right'

else:
    winner = "No winner! Equal time!"

print(f'The winner is {driver} with total time: {winner:.1f}')


""" __________ Car Race ____________


Write a program that announces the winner of a car race. 
You will receive a sequence of numbers.
Each number represents the time needed for the car to pass through that step (the index).

There will be two cars.
The first one starts from the left side, and the other one starts from the right side.
The middle index of the sequence is the finish line.

Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time).
If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).

The number of elements in the sequence will always be odd.

Print the result in the following format:
"The winner is {left/right} with total time: {total_time}".

The time should be formatted to the first decimal point.


______________ Test Data ______________


Input 1:
-------
29 13 9 0 13 0 21 0 14 82 12


Output 1:
--------
The winner is left with total time: 53.8


---------------------------------------


Input 2:
-------
123 20 4 0 13 0 0 5 5 14 0


Output 2:
--------
The winner is right with total time: 19.2


---------------------------------------
"""
