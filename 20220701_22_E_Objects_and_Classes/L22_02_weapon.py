# 20220701 - Python - Objects and Classes - Exercise
# 02 - Weapon - judge url: https://judge.softuni.org/Contests/Compete/Index/1734#1


# ----------------------- version 1 --------------------------  judge 100%


class Weapon:
    def __init__(self, bullets: int):
        self.bullets = bullets

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return 'shooting...'
        return 'no bullets left'

    def __repr__(self):
        return f'Remaining bullets: {self.bullets}'


weapon = Weapon(5)

print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
