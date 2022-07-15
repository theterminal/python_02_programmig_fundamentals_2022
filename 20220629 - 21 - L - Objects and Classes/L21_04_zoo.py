# 20220629 - Python Code - Objects and Classes - Lecture
# 04 - Zoo - judge url: https://judge.softuni.org/Contests/Practice/Index/1733#3


# ------------------ version 2 -------------------------


class Zoo:
    __animals = 0                           # local variable, cannot use outside of class Zoo

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1                  # must use 'Zoo.' in order to reach the variable

    def get_info(self, species):
        result = ''

        if species == 'mammal':
            result = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result = f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo = Zoo(input())
animal_count_entered = int(input())

for animal in range(animal_count_entered):
    animal_species, animal_name = input().split(' ')
    zoo.add_animal(animal_species, animal_name)

species_to_show = input()
print(zoo.get_info(species_to_show))


# ------------------ version 1 -------------------------


class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''

        if species == 'mammal':
            result = f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            result = f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            result = f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name_entered = input()
zoo = Zoo(zoo_name_entered)
animal_count_entered = int(input())

for animal in range(animal_count_entered):
    animal_species, animal_name = input().split(' ')
    zoo.add_animal(animal_species, animal_name)

species_to_show = input()
print(zoo.get_info(species_to_show))
