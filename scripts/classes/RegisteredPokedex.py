from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.Pokemon_class import Pokemon

class RegisteredPokedex(Pokedex):

    def __init__(self):
        super().__init__()
        self.encounters = {}  # pokemon_id -> count

    def register_encounter(self, pokemon: Pokemon):
        pid = pokemon.get_id()

        # Count encounter
        if pid not in self.encounters:
            self.encounters[pid] = 1
        else:
            self.encounters[pid] += 1

        # Add Pokémon only once
        if not any(p.get_id() == pid for p in self.get_pokemons()):
            new_list = self.get_pokemons() + [pokemon]
            new_list.sort(key=lambda p: p.get_id())
            self.set_pokemons(new_list)

    def get_encounter_count(self, pokemon: Pokemon):
        return self.encounters.get(pokemon.get_id(), 0)