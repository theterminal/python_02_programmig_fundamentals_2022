# 20220617 - Python Code - Lists Advance - Exercise
# 06 - Electron Distribution - judge: https://judge.softuni.org/Contests/Compete/Index/1731#5


num_electrons = int(input())

final_list = []
count_shells = 0

while True:
    count_shells += 1
    electrons_current_shell = 2 * (count_shells ** 2)

    if electrons_current_shell <= num_electrons:
        final_list.append(electrons_current_shell)
        num_electrons -= electrons_current_shell
    else:
        final_list.append(num_electrons)
        break

print(final_list)
