# 20220617 - Python Code - Lists Advance - Lecture
# 05 - Sorting Names - judge: https://judge.softuni.org/Contests/Practice/Index/1730#4


lst_names = input().split(', ')
lst_names_sorted = sorted(lst_names, key=lambda x: (-len(x), x))
print(lst_names_sorted)
