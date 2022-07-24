# 20220715 - Python Code - String Processing - Exercise
# 03 - Extract File - judge url: https://judge.softuni.org/Contests/Compete/Index/1740#2


# ------------------------ version 1 -------------------- judge: 100%


file_path = input().split('\\')
file_name, file_ext = file_path[-1].split('.')

print(f'File name: {file_name}')
print(f'File extension: {file_ext}')
