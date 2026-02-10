from Pokedex_class import Pokedex

class PokedexDisplay : 
    def __init__(self, pokedex : Pokedex) : 
        self.__pokedex = pokedex

    def get_pokedex(self) : 
        return self.__pokedex
    def set_pokedex(self, new_pokedex) :
        self.__pokedex = new_pokedex

    def draw_all_pokemons(self) : 
        for pokemon in self.get_pokedex.get_pokemons() : 
            pass

    