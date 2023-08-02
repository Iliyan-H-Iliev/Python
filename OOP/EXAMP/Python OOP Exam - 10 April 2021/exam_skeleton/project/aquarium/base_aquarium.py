from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []
        self.type = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if fish.type != self.type:
            return "Water not suitable."

        if self.capacity == len(self.fish):
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        res = [f"{self.name}:"]

        if not self.fish:
            res.append("Fish: none")

        else:
            res.append(f"Fish: {' '.join(f.name for f in self.fish)}")

        res.append(f"Decorations: {len(self.decorations)}")
        res.append(f"Comfort: {self.calculate_comfort()}")

        return "\n".join(res)


