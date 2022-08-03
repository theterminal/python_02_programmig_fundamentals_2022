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


""" ------------------ Heroes Of Code And Logic VII ---------------------------


You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic.
You want to play it all day long! So cancel all other arrangements and create your party!

On the first line of the standard input,
you will receive an integer 'n' – the number of heroes that you can choose for your party.

On the next 'n' lines,
the heroes themselves will follow with their hit points and mana points separated by a single space in the following format: 

"{hero name} {HP} {MP}"

    -	HP stands for hit points and MP for mana points
    -	a hero can have a maximum of 100 HP and 200 MP

After you have successfully picked your heroes, you can start playing the game.

You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 

There are several actions that the heroes can perform:
"CastSpell – {hero name} – {MP needed} – {spell name}"

    •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
        o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"

    •	If the hero is unable to cast the spell print:
        o	"{hero name} does not have enough MP to cast {spell name}!"

"TakeDamage – {hero name} – {damage} – {attacker}"

    •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
        o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"

    •	If the hero has died, remove him from your party and print:
        o	"{hero name} has been killed by {attacker}!"

"Recharge – {hero name} – {amount}"

    •	The hero increases his MP.
        If it brings the MP of the hero above the maximum value (200), MP is increased to 200.
        (the MP can't go over the maximum value).

    •	Print the following message:
        o   "{hero name} recharged for {amount recovered} MP!"

"Heal – {hero name} – {amount}"

    •	The hero increases his HP.
        If a command is given that would bring the HP of the hero above the maximum value (100),
        HP is increased to 100 (the HP can't go over the maximum value).

    •	Print the following message:
        o	"{hero name} healed for {amount recovered} HP!"


Input:
=====
    •	On the first line of the standard input, you will receive an integer 'n'

    •	On the following 'n' lines,
        the heroes themselves will follow with their hit points and mana points separated by a space in the following format

    •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given


Output:
======
    •	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):

"{hero name}
  HP: {current HP}
  MP: {current MP}"


Constraints:
===========
    •	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
    •	The HP/MP amounts in the commands will never be negative.
    •	The hero names in the commands will always be valid members of your party. No need to check that explicitly.


--------- Test Data -----------


Input 1:
-------
2
Solmyr 85 120
Kyrre 99 50
Heal - Solmyr - 10
Recharge - Solmyr - 50
TakeDamage - Kyrre - 66 - Orc
CastSpell - Kyrre - 15 - ViewEarth
End


Output 1:
--------
Solmyr healed for 10 HP!
Solmyr recharged for 50 MP!
Kyrre was hit for 66 HP by Orc and now has 33 HP left!
Kyrre has successfully cast ViewEarth and now has 35 MP!
Solmyr
  HP: 95
  MP: 170
Kyrre
  HP: 33
  MP: 35


-------------------------------


Input 2:
-------
4
Adela 90 150
SirMullich 70 40
Ivor 1 111
Tyris 94 61
Heal - SirMullich - 50
Recharge - Adela - 100
CastSpell - Tyris - 1000 - Fireball
TakeDamage - Tyris - 99 - Fireball
TakeDamage - Ivor - 3 - Mosquito
End


Output 2:
--------
SirMullich healed for 30 HP!
Adela recharged for 50 MP!
Tyris does not have enough MP to cast Fireball!
Tyris has been killed by Fireball!
Ivor has been killed by Mosquito!
Adela
  HP: 90
  MP: 200
SirMullich
  HP: 100
  MP: 40


-------------------------------
"""
