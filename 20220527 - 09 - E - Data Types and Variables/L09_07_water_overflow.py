# 20220527 - Python - Python Fundamentals - L9 - Data Types and Variables
# 07 - Water Overflow - judge url: https://judge.softuni.org/Contests/Compete/Index/1722#6


# --------- version 1 --------------------- judge 100%


num_lines = range(int(input()))
tank_capacity_l = 255
in_tank_l = 0

for _ in num_lines:
    l_to_pour_in_tank = float(input())

    if (tank_capacity_l - l_to_pour_in_tank) < 0:
        print('Insufficient capacity!')
        continue

    tank_capacity_l -= l_to_pour_in_tank
    in_tank_l += l_to_pour_in_tank

print(int(in_tank_l))


""" -------------- Water Overflow ---------------


You have a water tank with a capacity of 255 liters.
On the first line, you will receive 'n' – the number of lines, which will follow.
On the following 'n' lines, you will receive liters of water (integers), which you should pour into your tank.
If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
On the last line, print the liters in the tank.


--------------- Test Data ----------------


Input 1:
-------
5
20
100
100
100
20


Output 1:
--------
Insufficient capacity!
240


------------------------------------------


Input 2:
-------
7
10
20
30
10
5
10
20


Output 2:
--------
105


------------------------------------------


Input 3:
-------
1
1000


Output 3:
--------
Insufficient capacity!
0


------------------------------------------


Input 4:
-------
4
250
10
20
40


Output 4:
--------
Insufficient capacity!
Insufficient capacity!
Insufficient capacity!
250


-----------------------------------------

"""
