# 20220714 - Python - Dictionaries - Exercise
# 09 - Student Academy - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#8


# ------------------------- version 1 ------------------ judge: 100%


num_pairs_of_rows = int(input())
name = ''
db = {}
to_delete = []

for i in range(num_pairs_of_rows):
    name = input()
    grade = float(input())

    if name not in db:
        db[name] = [grade]
    else:
        db[name] += [grade]

for k, v in db.items():
    if (sum(v) / len(v)) < 4.5:
        to_delete.append(k)

for i in to_delete:
    db.pop(i)

for k, v in db.items():
    print(f'{k} -> {(sum(v) / len(v)):.2f}')
