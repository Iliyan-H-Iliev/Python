from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @staticmethod
    def find_obj(value, attribute, array):
        for obj in array:
            if getattr(obj, attribute) == value:
                return obj
        return None

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.HORSE_TYPES:
            return

        if self.find_obj(horse_name, "name", self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self.HORSE_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_obj(jockey_name, "name", self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.find_obj(race_type, "race_type", self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_obj(jockey_name, "name", self.jockeys)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]

        if not horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse = horses[-1]
        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.find_obj(race_type, "race_type", self.horse_races)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_obj(jockey_name, "name", self.jockeys)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.find_obj(race_type, "race_type", self.horse_races)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = race.jockeys[0]
        for jockey in race.jockeys:
            if jockey.horse.speed > winner.horse.speed:
                winner = jockey

        return (f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h "
                f"is {winner.name}! Winner's horse: {winner.horse.name}.")



