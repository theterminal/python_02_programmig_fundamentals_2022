# 20220615 - Python Code - Functions - More Exercise
# 01 - Data Types - judge url: https://judge.softuni.org/Contests/Practice/Index/1729#0


# -------------- version 1 -------------------------- judge 100%


def data_types(type_1, value_1):
    if type_1 == 'int':
        return int(value_1) * 2
    elif type_1 == 'real':
        return f'{(float(value_1) * 1.5):.2f}'
    elif type_1 == 'string':
        return f'${value_1}$'


type_in = input()
value_in = input()

print(data_types(type_in, value_in))


""" ____________ Data Types ____________


Write a function that, depending on the first line of the input, reads one of the following strings:
"int", "real", or "string".

•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".

Print the result on the console.


__________ Test Data ____________


Input 1:
-------
int
5


Output 1:
--------
10


---------------------------------


Input 2:
-------
real
2


Output 2:
--------
3.00


---------------------------------


Input 3:
--------
string
hello


Output 3:
--------
$hello$


---------------------------------
"""
