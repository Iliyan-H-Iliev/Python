from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            current_player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        current_player.guild = "Unaffiliated"
        self.players.remove(current_player)
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"

        for p in self.players:
            result += p.player_info()
        return result

