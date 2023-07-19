from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.height * self.width


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


class AreaCalculator:

    @property
    def shapes(self):
        return self.__shapes

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shape(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.calculate_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
