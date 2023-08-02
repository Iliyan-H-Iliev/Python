from typing import List

from project.people.child import Child


class Room:

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total_cost = 0
        for array in args:
            for el in array:
                total_cost += el.get_monthly_expense()

        self.expenses = total_cost


