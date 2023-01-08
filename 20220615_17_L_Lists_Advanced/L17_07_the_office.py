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
