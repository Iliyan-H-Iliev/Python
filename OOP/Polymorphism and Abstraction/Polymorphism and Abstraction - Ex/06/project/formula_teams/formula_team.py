from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses_per_race(self):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0

        for sponsor in self.sponsors:
            for pos, money in sponsor.items():
                if pos >= race_pos:
                    earned_money += money
                    break
        earned_money -= self.expenses_per_race
        self.budget += earned_money
        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"
