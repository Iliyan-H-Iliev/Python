from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        players = [x for x in args if x not in self.players]

        [self.players.append(x) for x in players]

        return f"Successfully added: {', '.join([x.name for x in players])}"

    def add_supply(self, *args):
        suppliers = [x for x in args]

        [self.supplies.append(x) for x in suppliers]

    def sustain(self, player_name, sustenance_type):

        if sustenance_type == "Food" or sustenance_type == "Drink" and \
                player_name in [x.name for x in self.players]:
            return self.sustaining(player_name, sustenance_type)

    def sustaining(self, player_name, sustenance_type):
        sustenance = [x for x in reversed(self.supplies) if x.type == sustenance_type]

        if not sustenance and sustenance_type == "Food":
            return "There are no food supplies left!"

        elif not sustenance and sustenance_type == "Drink":
            return "There are no drink supplies left!"

        player = [x for x in self.players if x.name == player_name][0]

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        player.stamina = min((player.stamina + sustenance[0].energy), 100)

        self.supplies.remove(sustenance[0])

        return f"{player_name} sustained successfully with {sustenance[0].name}."

    def duel(self, first_player_name, second_player_name):
        player1 = [x for x in self.players if x.name == first_player_name][0]
        player2 = [x for x in self.players if x.name == second_player_name][0]

        if player1.stamina == 0 and player2.stamina == 0:
            return f"{self.does_have_stamina(player1)}\n{self.does_have_stamina(player2)}"

        elif player1.stamina == 0:
            return self.does_have_stamina(player1)

        elif player2.stamina == 0:
            return self.does_have_stamina(player2)

        if player1.stamina <= player2.stamina:
            return self.dueling(player1, player2)

        else:
            return self.dueling(player2, player1)

    def next_day(self):
        for p in self.players:
            reduce_stamina_with = p.age * 2
            p.stamina = max(p.stamina - reduce_stamina_with, 0)

            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        return "\n".join(
            [str(p) for p in self.players]
                +
            [s.details() for s in self.supplies]
        )

    @staticmethod
    def does_have_stamina(player):
        return f"Player {player.name} does not have enough stamina."

    @staticmethod
    def dueling(first, second):
        second.stamina -= first.stamina // 2

        if second.stamina < 1:
            second.stamina = 0
            return f"Winner: {first.name}"

        first.stamina -= second.stamina // 2

        if first.stamina < 1:
            first.stamina = 0
            return f"Winner: {second.name}"

        if first.stamina > second.stamina:
            return f"Winner: {first.name}"

        else:

            return f"Winner: {second.name}"
