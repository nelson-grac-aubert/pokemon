from scripts.classes.Pokemon_class import Pokemon
from scripts.classes.Pokedex_class import Pokedex

class PlayerPokedex(Pokedex) : 
    
    def chose_as_combat_pokemon(self, chosen_pokemon : Pokemon) : 
        pass 
    
    def abandon_pokemon(self, abandonned_pokemon : Pokemon) : 
        self.get_pokemons().remove(abandonned_pokemon)