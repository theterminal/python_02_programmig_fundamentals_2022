# 20220706 - Python - Dictionaries - Lecture
# 04 - Students - judge url: https://judge.softuni.org/Contests/Practice/Index/1736#3


# --------------------- version 1 --------------------------- judge 100%


students = {}

while True:
    command = input()
    if command[0].islower():
        break

    tokens = command.split(':')

    student_name = tokens[0]
    student_id = tokens[1]
    student_course = tokens[2]

    students[student_id] = {student_name: student_course}

if '_' in command:
    command = command.replace('_', ' ')

for key, value in students.items():
    for key_2, value_2 in value.items():
        if command in value_2:
            print(key_2, '-', key)
