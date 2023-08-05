from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.band_members.musician import Musician
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}
    NEEDED_SKILLS = {
        "Rock":
            ["play the drums with drumsticks", "sing high pitch notes", "play rock"],
        "Metal":
            ["play the drums with drumsticks", "sing low pitch notes", "play metal"],
        "Jazz":
            ["play the drums with drum brushes", "sing high pitch notes",  "sing low pitch notes", "play jazz"]
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @staticmethod
    def find_object_by_name(name: str, collection: List):
        for musician in collection:
            if musician.name == name:
                return musician

    def find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def can_play_at_the_concert(self, band: Band, concert: Concert):
        skills = []

        for musician in band.members:
            skills.extend(musician.skills)

        for skill in self.NEEDED_SKILLS[concert.genre]:
            if skill not in skills:
                return False
        return True

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        if self.find_object_by_name(name, self.musicians):
            raise ValueError(f"{name} is already a musician!")

        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{musician.name} is now a {musician_type}."

    def create_band(self, name: str):
        if self.find_object_by_name(name, self.bands):
            raise ValueError(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{band.name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        found_concert = self.find_concert_by_place(place)
        if found_concert:
            raise ValueError(f"{place} is already registered for {found_concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{concert.genre} concert in {concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.find_object_by_name(musician_name, self.musicians)

        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.find_object_by_name(band_name, self.bands)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.find_object_by_name(band_name, self.bands)

        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.find_object_by_name(musician_name, band.members)

        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.find_object_by_name(band_name, self.bands)
        concert = self.find_concert_by_place(concert_place)

        band_members = []

        for member in band.members:
            if member.__class__.__name__ not in band_members:
                band_members.append(member.__class__.__name__)

        if len(band_members) < 3:
            raise Exception(f"{band.name} can't start the concert because it doesn't have enough members!")

        if not self.can_play_at_the_concert(band, concert):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."







