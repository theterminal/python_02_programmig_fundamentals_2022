# 20220714 - Python - Dictionaries - Exercise
# 10 - Company Users - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#9


# ------------------------ version 2 ----------------- judge: 100%


db = {}

while True:
    data_in = input()
    if data_in == 'End':
        break

    company, employee_id = data_in.split(' -> ')

    if company not in db:
        db[company] = [employee_id]
    else:
        if employee_id not in db[company]:
            db[company] += [employee_id]

for k, v in db.items():
    print(f'{k}')
    for e_id in v:
        print(f'-- {e_id}')


# ------------------------ version 1 ----------------- judge: 100%


db = {}

while True:
    data_in = input()

    if data_in == 'End':
        for k, v in db.items():
            print(f'{k}')
            for e_id in v:
                print(f'-- {e_id}')
        break

    company, employee_id = data_in.split(' -> ')

    if company not in db:
        db[company] = [employee_id]
    else:
        if employee_id not in db[company]:
            db[company] += [employee_id]
