from scripts.classes.Pokemon import Pokemon
from scripts.logic.json_management import load_pokemons_from_json, load_types_from_json

class Pokedex:
    def __init__(self):
        self.__pokemons = []
        self.type_data = {}

    def load_data(self, pokemon_json_path, types_json_path):
        self.type_data = load_types_from_json(types_json_path)
        self.__pokemons = load_pokemons_from_json(pokemon_json_path, self.type_data)
        for p in self.__pokemons:
            p._Pokemon__pokedex = self

    def get_pokemons(self):
        return sorted(self.__pokemons, key=lambda p: p.get_id())


    def set_pokemons(self, new_pokemons):
        self.__pokemons = new_pokemons
        for p in self.__pokemons:
            p._Pokemon__pokedex = self

    def get_pokemon_by_id(self, pid):
        for p in self.__pokemons:
            if p.get_id() == pid:
                return p
        return None

    def add_pokemon(self, new_pokemon: Pokemon):
        new_pokemon._Pokemon__pokedex = self
        self.__pokemons.append(new_pokemon)


kanto_pokedex = Pokedex()
kanto_pokedex.load_data(
    "assets/data/all_pokemons.json",
    "assets/data/all_types.json"
)