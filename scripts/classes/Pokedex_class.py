from scripts.classes.Pokemon_class import Pokemon

class Pokedex : 
    def __init__(self) : 
        self.__pokemons = []

    def get_pokemons(self) : 
        return self.__pokemons
    def set_pokemons(self, new_pokemons) :
        self.__pokemons = new_pokemons

    def add_pokemon(self, new_pokemon : Pokemon) : 
        """
        Add a pokemon to the Pokedex
        
        :param new_pokemon: The pokemon added to the pokedex
        :type new_pokemon: Pokemon
        """
        self.get_pokemons().append(new_pokemon)