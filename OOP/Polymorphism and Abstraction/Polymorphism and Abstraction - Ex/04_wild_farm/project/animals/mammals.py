from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    @property
    def gain_weight(self) -> float:
        return 0.10

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    @property
    def gain_weight(self) -> float:
        return 0.40

    @property
    def food_that_eats(self):
        return [Meat]


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    @property
    def gain_weight(self) -> float:
        return 0.30

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    @property
    def gain_weight(self) -> float:
        return 1.00

    @property
    def food_that_eats(self):
        return [Meat]
