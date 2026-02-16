from scripts.classes.Pokemon_class import Pokemon
from scripts.classes.Pokedex_class import Pokedex

class PlayerPokedex(Pokedex):

    def __init__(self):
        super().__init__()
        self.combat_pokemon = None

    def choose_as_combat_pokemon(self, chosen_pokemon: Pokemon):
        """Set the chosen Pokémon as the player's combat Pokémon."""
        self.combat_pokemon = chosen_pokemon

    def abandon_pokemon(self, abandoned_pokemon: Pokemon):
        """Remove a Pokémon from the player's pokedex."""
        if abandoned_pokemon in self.get_pokemons():
            self.get_pokemons().remove(abandoned_pokemon)