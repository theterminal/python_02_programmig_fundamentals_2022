# 20220601 - Python - L11 - Lists - Basics
# 02 - Courses - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#1


# --------------------- version 1 -------------------------- judge 100%


num_lines = int(input())
course_list = list()

for _ in range(num_lines):
    course_name_entered = input()
    course_list.append(course_name_entered)

print(course_list)


# --------------------- version 2 -------------------------- judge 100%


num_lines = int(input())
course_list = list()

for _ in range(num_lines):
    course_name_entered = input()
    course_list += [course_name_entered]

print(course_list)
