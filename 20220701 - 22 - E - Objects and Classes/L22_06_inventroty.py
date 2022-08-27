# 20220701 - Python - Objects and Classes - Exercise
# 06 - Inventory - judge url: https://judge.softuni.org/Contests/Compete/Index/1734#5


# ------------------------- version 1 ---------------------------- judge 100%


class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return f'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity - len(self.items)
        return f"Items: {', '.join(self.items)}.\nCapacity left: {left_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
