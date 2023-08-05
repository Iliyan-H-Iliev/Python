from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES_TYPE = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth" : OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    @staticmethod
    def find_obj(name, parameter, collection):
        for obj in collection:
            if getattr(obj, parameter) == name:
                return obj

    @staticmethod
    def get_the_bill(booth: Booth):

        bill = booth.price_for_reservation

        for delicacy in booth.delicacy_orders:
            bill += delicacy.price

        return bill

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if self.find_obj(name, "name", self.delicacies):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES_TYPE:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        self.delicacies.append(self.VALID_DELICACIES_TYPE[type_delicacy](name, price))
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if self.find_obj(booth_number, "booth_number", self.booths):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        self.booths.append(self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity))
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        delicacy = self.find_obj(delicacy_name, "name", self.delicacies)
        booth = self.find_obj(booth_number, "booth_number", self.booths)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_obj(booth_number, "booth_number", self.booths)
        bill = self.get_the_bill(booth)
        self.income += bill
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."






