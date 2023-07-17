from project.controller import Controller
from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food

controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
turd_player = Player('Aslan', 12, 94)
print(juice.details())
print(apple.details())

print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# print(controller.find_player_by_name("hamko"))


first_player.stamina = 10
second_player.stamina = 25
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
