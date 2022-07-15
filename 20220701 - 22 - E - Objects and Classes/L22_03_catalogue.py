# 20220701 - Python Code - Objects and Classes - Exercise
# 03 - Catalogue - judge url: https://judge.softuni.org/Contests/Compete/Index/1734#2


# ------------------------ version 2 ----------------------------------


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        return f'Items in the {self.name} catalogue:\n' + '\n'.join(sorted(self.products))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)


# ------------------------ version 1 ----------------------------------


class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        # return [self.products[i] for i in range(len(self.products)) if self.products[i][0] == first_letter]
        # return [product for product in self.products if product[0] == first_letter]
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        string_to_return = f'Items in the {self.name} catalogue:\n'
        string_to_return += '\n'.join(sorted(self.products))
        return string_to_return


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
