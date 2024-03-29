# 20220629 - Python - Objects and Classes - Lecture
# Note 01 - Class and Object


class Person:
    def __init__(self, first_name, last_name, age=21):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f'Hello {self.first_name} {self.last_name} {self.age}'


person_1 = Person('Ivan', 'Dragan', 32)
print(person_1.first_name, person_1.age)

person_2 = Person('Kiril', 'Popov')
print(person_2.last_name, person_2.age)

print(person_1.say_hello())
