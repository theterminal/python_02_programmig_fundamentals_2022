# 20220618 - Python - Lists Advance - Lecture
# 07 - The Office - judge: https://judge.softuni.org/Contests/Practice/Index/1730#6


# ----------------- version 1 ------------------- judge 100%


emp_start_hap = list(map(int, input().split(' ')))
factor = int(input())

emp_hap_w_factor = [x * factor for x in emp_start_hap]
average_hap = sum(emp_hap_w_factor) / len(emp_hap_w_factor)
count_hap = len([x for x in emp_hap_w_factor if x >= average_hap])

if count_hap >= len(emp_start_hap) / 2:
    print(f'Score: {count_hap}/{len(emp_start_hap)}. Employees are happy!')
else:
    print(f'Score: {count_hap}/{len(emp_start_hap)}. Employees are not happy!')


"""______________ The Office _____________


You will receive two lines of input: 
    •	a list of employees' happiness as a string of numbers separated by a single space 
    •	a happiness improvement factor (single number).
    
Your task is to find out if the employees are generally happy in their office.

First, multiply each employee's happiness by the factor.
Then, print one of the following lines:

    •	If half or more of the employees have happiness greater than or equal to the average:
        "Score: {happy_count}/{total_count}. Employees are happy!"
        
    •	Otherwise:
        "Score: {happy_count}/{total_count}. Employees are not happy!"


______________ Test Data ____________


Input 1:
-------
1 2 3 4 2 1
3


Output 1:
--------
Score: 2/6. Employees are not happy!


-------------------------------------


Input 2:
-------
2 3 2 1 3 3
4


Output 2:
--------
Score: 3/6. Employees are happy!


-------------------------------------
"""
