class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def pizza_is_prepared(self):
        return f"Pizza {self.name} already prepared, and we can\'t make any changes!"

    def price_change(self, s, ingredient, quantity, price_per_quantity):
        if s == "+":
            self.ingredients[ingredient] += quantity
            self.price += quantity * price_per_quantity
        elif s == "-":
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * price_per_quantity

    def pizza_ingredients(self):
        result = []
        for k, v in self.ingredients.items():
            result.append(f"{k}: {v}")

        return result

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return self.pizza_is_prepared()

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.price_change("+", ingredient, quantity, price_per_quantity)

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):

        if self.ordered:
            return self.pizza_is_prepared()

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.price_change("-", ingredient, quantity, price_per_quantity)

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(x for x in self.pizza_ingredients())} and " \
               f"the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))