# 20220701 - Python - Objects and Classes - Exercise
# 01 - Storage - judge url: https://judge.softuni.org/Contests/Compete/Index/1734#0


# ----------------------- version 2 ----------------------------- judge 100%


class Storage:
    storage = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            Storage.storage.append(product)
            self.capacity -= 1

    def get_products(self):
        return Storage.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")

print(storage.get_products())


# ----------------------- version 1 --------------------------  judge 100%
# This version will work only if there is one object. If more than 1 object it is not correct!


class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if len(self.storage) < self.capacity:
            self.storage.append(product)

    def get_products(self):
        return self.storage


storage = Storage(4)
storage.add_product("apple")
storage.add_product("banana")
storage.add_product("potato")
storage.add_product("tomato")
storage.add_product("bread")

print(storage.get_products())
