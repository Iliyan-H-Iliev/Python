from project.player import Player
from typing import List

from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def __str__(self):
        res = "\n".join([str(p) for p in self.players])

        if self.supplies:
            res += "\n"

        res += "\n".join([str(s.details()) for s in self.supplies])

        return res

    def add_player(self, *players: Player):
        added_players = []

        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)

        return f"Successfully added: {', '.join([n for n in added_players])}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def find_player_by_name(self, name: str):
        try:
            player = [p for p in self.players if p.name == name][0]
        except IndexError:
            return None
        return player

    def find_supply_ind_by_type(self, name: str):

        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].__class__.__name__ == name:
                return i

        return None

    def attacking(self, player_1: Player, player_2: Player):
        player_1.stamina = max(player_1.stamina - (player_2.stamina / 2), 0)
        if player_1.stamina == 0:
            return f"Winner: {player_2.name}"

        player_2.stamina = max(player_2.stamina - (player_1.stamina / 2), 0)
        if player_2.stamina == 0:
            return f"Winner: {player_1.name}"

        return f"Winner: {self.check_the_winner(player_1, player_2).name}"

    def sustain(self, player_name: str, sustenance_name: str):
        player = self.find_player_by_name(player_name)
        if not player or sustenance_name not in ["Food", "Drink"]:
            return

        supply_ind = self.find_supply_ind_by_type(sustenance_name)
        self.supply_check(supply_ind, sustenance_name)

        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        supply = self.supplies.pop(supply_ind)
        player.stamina = min(player.stamina + supply.energy, 100)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, player_1_name: str, player_2_name: str):
        player_1 = self.find_player_by_name(player_1_name)
        player_2 = self.find_player_by_name(player_2_name)

        check_stamina = self.is_stamina_0(player_1, player_2)

        if check_stamina:
            return check_stamina

        if player_1.stamina > player_2.stamina:
            return self.attacking(player_1, player_2)
        else:
            return self.attacking(player_2, player_1)

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    @staticmethod
    def supply_check(ind: int, name: str):
        if not isinstance(ind, int):
            if name == "Food":
                raise Exception("There are no food supplies left!")
            elif name == "Drink":
                raise Exception("There are no drink supplies left!")

    @staticmethod
    def is_stamina_0(player_1: Player, player_2: Player):
        res = ""
        if player_1.stamina == 0:
            res += f"Player {player_1.name} does not have enough stamina."
        if player_2.stamina == 0:
            res += f"\nPlayer {player_2.name} does not have enough stamina."
        return res

    @staticmethod
    def check_the_winner(player_1: Player, player_2: Player):
        if player_1.stamina > player_2.stamina:
            return player_1
        return player_2
