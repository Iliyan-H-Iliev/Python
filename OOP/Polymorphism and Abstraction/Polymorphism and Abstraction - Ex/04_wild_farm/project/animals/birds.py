from project.animals.animal import Bird
from project.food import Fruit, Seed, Vegetable, Meat


class Owl(Bird):

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def gain_weight(self) -> float:
        return 0.25

    @property
    def food_that_eats(self):
        return [Meat]


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    @property
    def gain_weight(self) -> float:
        return 0.35

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]
