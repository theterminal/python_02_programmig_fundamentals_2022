# 20220714 - Python Code - Dictionaries - Exercise
# 08 - Courses - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#7


# ------------------- version 1 ----------------------- judge: 100%


db = {}

while True:
    command = input()
    if command == 'end':
        break

    course, name = command.split(' : ')

    if course not in db:
        db[course] = [name]
    else:
        db[course] += [name]

for k, v in db.items():
    print(f'{k}: {len(v)}')
    for student in v:
        print(f'-- {student}')
