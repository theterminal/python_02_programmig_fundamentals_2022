# 20220629 - Python Code - Objects and Classes - Lecture
# Notes 03


class Person:
    def __init__(self, first_name, last_name, age=21):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self):
        return f'Hello {self.first_name} {self.last_name} {self.age}'


person = Person('Ivan', 'Dragan', 32)
print(person.first_name, person.age)

person.age += 10
print(person.age)
