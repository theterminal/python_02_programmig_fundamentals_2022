# 20220629 - Python Code - Objects and Classes - Lecture
# 05 - Circle - judge url: https://judge.softuni.org/Contests/Practice/Index/1733#4


# ------------------------ version 1 -----------------------------


class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * (self.radius ** 2)

    def calculate_area_of_sector(self, angle):
        return angle / 360 * (Circle.__pi * (self.radius * self.radius))


circle = Circle(10)
angle_entered = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle_entered):.2f}")
