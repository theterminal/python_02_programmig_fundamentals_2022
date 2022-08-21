# 20220621 - Python - Mid Exam Preparation
# 01 - Counter-Strike - judge url: https://judge.softuni.org/Contests/Practice/Index/2305#0


# ---------------- version 01 ------------------------------ judge 100%


energy = int(input())                                               # int [1:10_000]
battles_won = 0

while True:
    distance = input()                                              # int [1:10_1000]

    if distance == 'End of battle':
        print(f'Won battles: {battles_won}. Energy left: {energy}')
        break
    else:
        distance = int(distance)

    if distance <= energy:
        battles_won += 1
        energy -= distance
        if battles_won % 3 == 0:
            energy += battles_won
    else:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        break
