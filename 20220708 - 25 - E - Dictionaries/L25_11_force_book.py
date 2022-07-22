# 20220714 - Python Code - Dictionaries - Exercise
# 11 - * Force Book - judge url: https://judge.softuni.org/Contests/Compete/Index/1737#10


# --------------------------- version 2 --------------------------- judge: 100%


db = {}

while True:
    data_in = input()
    if data_in == 'Lumpawaroo':
        break

    if '|' in data_in:
        side, user = data_in.split(' | ')
        present = False

        for v in db.values():
            if user in v:
                break
        else:
            if side not in db.keys():
                db[side] = [user]
            else:
                db[side].append(user)

    elif '->' in data_in:
        user, side = data_in.split(' -> ')

        for k, v in db.items():
            if user in v:
                db[k].pop(v.index(user))
                break

        if side not in db.keys():
            db[side] = [user]
        else:
            db[side] += [user]

        print(f'{user} joins the {side} side!')

for k in db.keys():
    if len(db[k]) > 0:
        print(f'Side: {k}, Members: {len(db[k])}')
        [print(f'! {user}') for user in db[k]]


# --------------------------- version 1 --------------------------- judge: 100%


db = {}

while True:
    data_in = input()
    if data_in == 'Lumpawaroo':
        break

    if '|' in data_in:
        side, user = data_in.split(' | ')
        present = False

        for value in db.values():
            if user in value:
                present = True
                break

        if not present:
            if side not in db.keys():
                db[side] = [user]
            else:
                db[side].append(user)

    elif '->' in data_in:
        user, side = data_in.split(' -> ')

        for k, v in db.items():
            if user in v:
                db[k].pop(v.index(user))
                break

        if side not in db.keys():
            db[side] = [user]
        else:
            db[side] += [user]

        print(f'{user} joins the {side} side!')

for side in db.keys():
    if len(db[side]) > 0:
        print(f'Side: {side}, Members: {len(db[side])}')
        [print(f'! {user}') for user in db[side]]
