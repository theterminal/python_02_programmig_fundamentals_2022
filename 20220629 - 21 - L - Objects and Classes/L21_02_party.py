# 20220629 - Python Code - Objects and Classes - Lecture
# 02 - Party - judge url: https://judge.softuni.org/Contests/Practice/Index/1733#1


class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()
    if command == 'End':
        break

    party.people.append(command)

print(f'Going: {", ".join(party.people)}')
print(f'Total: {len(party.people)}')
