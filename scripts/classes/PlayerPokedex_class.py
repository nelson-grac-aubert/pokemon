from scripts.classes.Pokemon_class import Pokemon
from scripts.classes.Pokedex_class import Pokedex

class PlayerPokedex(Pokedex) : 
    
    def abandon_pokemon(self, abandonned_pokemon : Pokemon) : 
        self.get_pokemons().remove(abandonned_pokemon)