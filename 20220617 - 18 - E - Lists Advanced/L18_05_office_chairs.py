# 20220617 - Python - Lists Advance - Exercise
# 05 - Office Chairs - judge: https://judge.softuni.org/Contests/Compete/Index/1731#4


# ---------------- version 3 ---------------------- judge 100%


def check_chairs(num_rooms):
    chairs_total_free = 0
    chairs_needed = 0

    for current_room in range(1, num_rooms + 1):
        free_chairs, visitors = input().split()
        diff = len(free_chairs) - int(visitors)

        if diff >= 0:
            chairs_total_free += diff
        else:
            chairs_needed += abs(diff)
            print(f'{abs(diff)} more chairs needed in room {current_room}')

    return chairs_total_free, chairs_needed


num_rooms_given = int(input())
total_available_chairs, need_chairs = check_chairs(num_rooms_given)

if total_available_chairs >= need_chairs:
    print(f'Game On, {total_available_chairs} free chairs left')


# ---------------- version 2 ---------------------- judge 100%


num_rooms = int(input())

flag = False
total_free_chairs = total_chairs = total_people = 0

for i in range(1, num_rooms + 1):
    num_chairs_current_room, num_people_current_room = input().split()
    total_chairs += len(num_chairs_current_room)
    total_people += int(num_people_current_room)

    if len(num_chairs_current_room) < int(num_people_current_room):
        print(f'{int(num_people_current_room) - len(num_chairs_current_room)} more chairs needed in room {i}')
        flag = True

total_free_chairs = total_chairs - total_people

if not flag:
    print(f'Game On, {total_free_chairs} free chairs left')


# ---------------- version 1 ---------------------- judge 100%


num_rooms = int(input())
flag = False
total_free_chairs = 0
total_chairs = 0
total_people = 0

for i in range(1, num_rooms + 1):
    info = input().split()
    num_chairs_current_room = len(info[0])
    num_people_current_room = int(info[1])
    total_chairs += num_chairs_current_room
    total_people += num_people_current_room

    if num_chairs_current_room < num_people_current_room:
        print(f'{num_people_current_room - num_chairs_current_room} more chairs needed in room {i}')
        flag = True

total_free_chairs = total_chairs - total_people

if not flag:
    print(f'Game On, {total_free_chairs} free chairs left')


""" ____________ Office Chairs ____________


You are a facility manager at a large business center.
One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.

On the first line, you will be given an integer 'n' representing the number of rooms in the business center.
On the following 'n' lines for each room, you will receive information about the chairs in the room and the number of visitors.
Each chair will be presented with the char "X".
Next, there will be a single space and the number of visitors at the end.
For example: "XXXXX 4" (5 chairs and 4 visitors).

Keep track of the free chairs:
    •	If there are not enough chairs in a specific room, print the following message:
        "{needed_chairs_in_room} more chairs needed in room {number_of_room}".
        The rooms start from 1.
        
    •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".


__________ Test Data ___________


Input 1:
-------
4
XXXX 4
XX 1
XXXXXX 3
XXX 3


Output 1:
--------
Game On, 4 free chairs left


-------------------------------


Input 2:
-------
3
XXXXXXX 5
XXXX 5
XXXXXX 8


Output 2:
--------
1 more chairs needed in room 2
2 more chairs needed in room 3


-------------------------------
"""
