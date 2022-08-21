# 20220617 - Python - Lists Advance - Exercise
# 06 - Electron Distribution - judge: https://judge.softuni.org/Contests/Compete/Index/1731#5


# ------------------- version 1 ------------------- judge 100%


num_electrons = int(input())
final_list = []
count_shells = 0

while num_electrons > 0:
    count_shells += 1
    electrons_current_shell = 2 * (count_shells ** 2)

    if electrons_current_shell <= num_electrons:
        final_list.append(electrons_current_shell)
        num_electrons -= electrons_current_shell
    else:
        final_list.append(num_electrons)
        break

print(final_list)



""" ___________ Electron Distribution _______________


You are a mad scientist, and you have decided to play with electron distribution among atom shells.
The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of electrons.

You will receive a single integer - the number of electrons.
Your task is to fill shells until there are no more electrons left.

The rules for electron distribution are as follows:

    •	The maximum number of electrons in a shell can be '2n2', where 'n' is the position of a shell (starting from 1).
        For example, the maximum number of electrons in the 3rd shield can be 2*3^2 = 18.

    •	You should start filling the shells from the first one at the first position.

    •	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following shell and so on.

In the end, print a list with the filled shells.


________ Test Data _______


Input 1:
-------
10


Output 1:
--------
[2, 8]


--------------------------


Input 2:
--------
44


Output 2:
---------
[2, 8, 18, 16]


--------------------------
"""
