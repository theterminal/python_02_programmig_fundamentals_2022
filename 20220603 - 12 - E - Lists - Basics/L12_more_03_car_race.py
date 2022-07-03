# 22020624 - Python Code - L12 - Lists Basics - More Exercise
# 03 - Car Race - judge url: https://judge.softuni.org/Contests/Practice/Index/1726#2


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
