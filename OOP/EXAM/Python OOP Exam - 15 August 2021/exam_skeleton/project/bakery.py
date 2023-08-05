from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    FOOD_TYPES = {"Bread": Bread, "Cake": Cake}
    DRINK_TYPES = {"Tea": Tea, "Water": Water}
    TABLE_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.food_menu_by_name = []
        self.drinks_menu: List[Drink] = []
        self.drinks_menu_by_name = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @staticmethod
    def find_product(name, repository):
        products = [p for p in repository if p.name == name]
        return products[0]

    def find_table(self, table_number):
        tables = [t for t in self.tables_repository if t.table_number == table_number]

        if not tables:
            return f"Could not find table {table_number}"

        return tables[0]

    def order_info(self, table_number, in_menu, not_in_menu):
        res = [f"Table {table_number} ordered:"]

        for product in in_menu:
            res.append(str(product))

        res.append(f"{self.name} does not have in the menu:")

        for name in not_in_menu:
            res.append(name)

        return res

    def find_product_in_menu_by_name(self, names, repository_names, repository_onj):
        in_menu = []
        not_in_menu = []
        for name in names:
            if name in repository_names:
                food = self.find_product(name, repository_onj)
                in_menu.append(food)
            else:
                not_in_menu.append(name)

        return in_menu, not_in_menu

    def add_food(self, food_type: str, name: str, price: float):

        if food_type not in Bakery.FOOD_TYPES:
            return

        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        self.food_menu.append(Bakery.FOOD_TYPES[food_type](name, price))
        self.food_menu_by_name.append(name)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in Bakery.DRINK_TYPES:
            return

        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        self.drinks_menu.append(Bakery.DRINK_TYPES[drink_type](name, portion, brand))
        self.drinks_menu_by_name.append(name)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in Bakery.TABLE_TYPES:
            return

        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        self.tables_repository.append(Bakery.TABLE_TYPES[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        tables = [t for t in self.tables_repository if t.capacity >= number_of_people and not t.is_reserved]

        if not tables:
            return f"No available table for {number_of_people} people"

        tables[0].reserve(number_of_people)
        return f"Table {tables[0].table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = self.find_table(table_number)

        if isinstance(table, str):
            return table

        in_menu, not_in_menu = self.find_product_in_menu_by_name(args, self.food_menu_by_name, self.food_menu)
        table.food_orders.extend(in_menu)

        res = self.order_info(table_number, in_menu, not_in_menu)

        return "\n".join(res)

    def order_drink(self, table_number: int, *args):

        table = self.find_table(table_number)

        if isinstance(table, str):
            return table

        in_menu, not_in_menu = self.find_product_in_menu_by_name(args, self.drinks_menu_by_name, self.drinks_menu)
        table.drink_orders.extend(in_menu)

        res = self.order_info(table_number, in_menu, not_in_menu)

        return "\n".join(res)

    def leave_table(self, table_number: int):

        table = self.find_table(table_number)

        if isinstance(table, str):
            return table

        bill = table.get_bill()
        table.clear()
        self.total_income += bill

        return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):

        res = []

        for table in self.tables_repository:
            if not table.is_reserved:
                res.append(table.free_table_info())

        return "\n".join(res)

    def get_total_income(self):

        return f"Total income: {self.total_income:.2f}lv"
