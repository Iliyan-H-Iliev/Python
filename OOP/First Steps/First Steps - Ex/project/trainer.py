from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_n: Pokemon):
        if pokemon_n not in self.pokemons:
            self.pokemons.append(pokemon_n)
            return f"Caught {pokemon_n.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for pok in self.pokemons:
            if pok.name == pokemon_name:
                self.pokemons.remove(pok)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"

        return result
