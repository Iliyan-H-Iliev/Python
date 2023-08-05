from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium_types = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}

        if aquarium_type not in aquarium_types:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium_types[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def find_aquarium(self, aquarium_name):
        aquariums = [a for a in self.aquariums if a.name == aquarium_name]
        if not aquariums:
            return None
        return aquariums[0]

    def add_decoration(self, decoration_type: str):
        decoration_types = {"Ornament": Ornament, "Plant": Plant}

        if decoration_type not in decoration_types:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration_types[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.find_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if isinstance(decoration, str) or not aquarium:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium.decorations.append(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish_types = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
        aquarium = self.find_aquarium(aquarium_name)

        if fish_type not in fish_types or not aquarium:
            return f"There isn't a fish of type {fish_type}."

        res = aquarium.add_fish(fish_types[fish_type](fish_name, fish_species, price))
        return res

    def feed_fish(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)

        for fish in aquarium.fish:
            fish.eat()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.find_aquarium(aquarium_name)

        value = sum(f.price for f in aquarium.fish)
        value += sum(d.price for d in aquarium.decorations)

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        res = []

        for aquarium in self.aquariums:
            res.append(str(aquarium))

        return "\n".join(res)

