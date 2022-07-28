# 20220722 - Python Code - Regular Expressions - Exercise
# 01 - Capture Numbers - judge url: https://judge.softuni.org/Contests/Compete/Index/1743#0

import re
# use this to construct the regex: https://regex101.com/


# ------------------------ version 1 -------------------- judge: 100%


pattern = r'\d+'

while True:
    line = input()
    if line:
        matches = re.findall(pattern, line)
        if matches:
            print(' '.join(matches), end=' ')
    else:
        break


''' ----------------------- Capture Numbers ---------------------------


Write a program that receives strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.


----------- Examples -----------


Input 1:
--------
The300
What is that?
I think it's the 3rd movie 
Let's watch it at 22:45


Output 1:
---------
300 3 22 45


---------------------------------


Input 2:
--------
123a456
789b987
654c321
0


Output 2:
---------
123 456 789 987 654 321 0


---------------------------------


Input 3:
--------
Let's go11!!!11!
Okey!1!


Output 3:
--------
11 11 1


'''