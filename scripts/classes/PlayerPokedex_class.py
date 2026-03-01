from scripts.classes.Pokemon_class import Pokemon
from scripts.classes.Pokedex_class import Pokedex

class PlayerPokedex(Pokedex):

    def __init__(self):
        super().__init__()
        self.combat_pokemon = None

    def choose_as_combat_pokemon(self, chosen_pokemon: Pokemon):
        """Set the chosen Pokémon as the player's combat Pokémon."""
        for p in self.get_pokemons():
            if p.get_id() == chosen_pokemon.get_id():
                self.combat_pokemon = p
                return


    def abandon_pokemon(self, abandoned_pokemon: Pokemon):
        """Remove a Pokémon from the player's pokedex."""
        if abandoned_pokemon in self.get_pokemons():
            self.get_pokemons().remove(abandoned_pokemon)

    def replace_combat_pokemon(self, new_pokemon):
        """Replace the current combat Pokémon with a new one."""
        index = self.get_pokemons().index(self.combat_pokemon)
        self.get_pokemons()[index] = new_pokemon
        self.combat_pokemon = new_pokemon
