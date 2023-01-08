# 20220731 - Python - Exam Preparation
# 03 - Heroes Of Code And Logic VII - judge url: https://judge.softuni.org/Contests/Practice/Index/2303#0


# ------------------------- version 1 --------- no functions ------- judge: 100%


num_heroes = int(input())
heroes_dict = {}

for i in range(num_heroes):
    data = input()
    name, hp, mp = data.split(' ')
    heroes_dict[name] = [int(hp), int(mp)]

while True:
    command = input()
    if command == 'End':
        break

    command = command.split(' - ')
    action = command[0]
    name = command[1]

    if action == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[3]

        if heroes_dict[name][1] >= mp_needed:
            heroes_dict[name][1] -= mp_needed
            print(f'{name} has successfully cast {spell_name} and now has {heroes_dict[name][1]} MP!')
        else:
            print(f'{name} does not have enough MP to cast {spell_name}!')

    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]

        heroes_dict[name][0] -= damage
        if heroes_dict[name][0] > 0:
            print(f'{name} was hit for {damage} HP by {attacker} and now has {heroes_dict[name][0]} HP left!')
        else:
            print(f'{name} has been killed by {attacker}!')
            del heroes_dict[name]

    elif action == 'Recharge':
        amount = int(command[2])

        if amount > (200 - heroes_dict[name][1]):
            print(f'{name} recharged for {200 - heroes_dict[name][1]} MP!')
            heroes_dict[name][1] = 200
        else:
            print(f'{name} recharged for {amount} MP!')
            heroes_dict[name][1] += amount

    elif action == 'Heal':
        amount = int(command[2])

        if amount > (100 - heroes_dict[name][0]):
            print(f'{name} healed for {100 - heroes_dict[name][0]} HP!')
            heroes_dict[name][0] = 100
        else:
            print(f'{name} healed for {amount} HP!')
            heroes_dict[name][0] += amount

for k, v in heroes_dict.items():
    print(k)
    print(f'  HP: {v[0]}')
    print(f'  MP: {v[1]}')


# ------------------------- version 2 ----- with functions -------- judge: 100%


def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name = data[0]
        hp = int(data[1])
        mp = int(data[2])
        heroes_dict[hero_name] = [hp, mp]
    return heroes_dict


def playing_game(heroes_dict):
    while True:
        command = input()
        if command == 'End':
            break

        command = command.split(' - ')
        action = command[0]
        hero_name = command[1]

        if action == 'CastSpell':
            mp_needed = int(command[2])
            spell_name = command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name][1]} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif action == 'TakeDamage':
            damage = int(command[2])
            attacker = command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]

                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif action == 'Recharge':
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif action == 'Heal':
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")

    return heroes_dict


def print_function(heroes_dict):
    for hero in heroes_dict:
        print(hero)
        print(f'  HP: {heroes_dict[hero][0]}')
        print(f'  MP: {heroes_dict[hero][1]}')


def heroes_of_code():
    n = int(input())
    hero_dict = {}  # In heroes_dict we have {name: [HP, MP]}

    create_heroes(hero_dict, n)
    playing_game(hero_dict)
    print_function(hero_dict)


heroes_of_code()
