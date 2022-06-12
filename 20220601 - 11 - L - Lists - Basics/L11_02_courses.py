# 20220601 - Python Code - L11 - Lists - Basics
# 02 - Courses - judge url: https://judge.softuni.org/Contests/Practice/Index/1724#1

num_lines = int(input())
course_list = list()

for _ in range(num_lines):
    course_name_entered = input()
    course_list.append(course_name_entered)

print(course_list)

# ---------- version 2 ---------------------

num_lines = int(input())
course_list = list()

for _ in range(num_lines):
    course_name_entered = input()
    course_list += [course_name_entered]

print(course_list)

# ---------- something else interesting ----

num_lines = int(input())
course_list = list()

for _ in range(num_lines):
    course_name_entered = input()
    course_list += course_name_entered

print(course_list)
print(type(course_list))
print(len(course_list))
