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


""" ------------- Courses ---------------


On the first line, you will receive a single number 'n'.
On the following 'n' lines, you will receive names of courses.
You should create a list of courses and print it.


----------- Test Data --------------


Input 1:
-------
2
PB Python
PF Python


Output 1:
--------
['PB Python', 'PF Python']


------------------------------------


Input 2:
-------
4
Front-End
C# Web
JS Core
Programming Fundamentals


Output 2:
--------
['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']


------------------------------------

"""
