import pygame
import random
from scripts.classes.PokemonType_class import PokemonType
from scripts.logic.assets_management import load_gif


class Pokemon : 
    def __init__(self, id : str, name : str, hp : int, attack : int, defense : int, speed : int, precision : int, types : list, can_evolve : bool, evolution_level : int, evolution_pokemon : list) : 
        """
        Docstring for __init__
        
        :param id: The id of that pokemon in a 3 digit format, used to get the sprites files
        :type id: str
        :param name: The name of that Pokemon
        :type name: str
        :param max hp: The maximum health points of that Pokemon
        :type max hp: int
        :param attack: The attack rating of that Pokemon
        :type attack: int
        :param defense: The defense rating of that Pokemon
        :type defense: int
        :param types: A list of the Types of that Pokemon
        :type types: list
        :param can_evolve: A boolean defining if that Pokemon can evolve
        :type can_evolve: bool
        :param evolution_level: The level at which that Pokemon can evolve
        :type evolution_level: int
        :param evolution_pokemon: The pokemons in which that Pokemon can evolve
        :type evolution_pokemon: list
        """

        self.__id = id
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__speed = speed
        self.__precision = precision
        self.__level = 1
        self.__exp = 0
        self.__types = types
        self.__can_evolve = can_evolve
        self.__evolution_level = evolution_level
        self.__evolution_pokemon = evolution_pokemon

        # Gif animation variables
        self.front_frames = []
        self.back_frames = []
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_speed = 3 
        self.scale = 1.0      

    # Getters and setters -----------------------------------------------------------------------------------------------

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        if not isinstance(new_id, str):
            raise TypeError("Name must be a string.")
        if new_id.strip() == "":
            raise ValueError("Name cannot be empty.")
        self.__id = new_id


    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        if new_name.strip() == "":
            raise ValueError("Name cannot be empty.")
        self.__name = new_name


    def get_max_hp(self):
        return self.__max_hp
    def set_max_hp(self, new_max_hp):
        if not isinstance(new_max_hp, int):
            raise TypeError("Max HP must be an integer.")
        if new_max_hp < 0:
            raise ValueError("Max HP cannot be negative.")
        self.__max_hp = new_max_hp


    def get_hp(self):
        return self.__hp
    def set_hp(self, new_hp):
        if not isinstance(new_hp, int):
            raise TypeError("HP must be an integer.")
        self.__hp = new_hp


    def get_attack(self):
        return self.__attack
    def set_attack(self, new_attack):
        if not isinstance(new_attack, int):
            raise TypeError("Attack must be an integer.")
        if new_attack < 0:
            new_attack = 0
        self.__attack = new_attack


    def get_defense(self):
        return self.__defense
    def set_defense(self, new_defense):
        if not isinstance(new_defense, int):
            raise TypeError("Defense must be an integer.")
        if new_defense < 0:
            raise ValueError("Defense cannot be negative.")
        self.__defense = new_defense

    def get_speed(self):
        return self.__speed
    def set_speed(self, new_speed):
        if not isinstance(new_speed, int):
            raise TypeError("Speed must be an integer.")
        if new_speed < 0:
            raise ValueError("Speed cannot be negative.")
        self.__speed = new_speed

    def get_precision(self):
        return self.__precision
    def set_precision(self, new_precision):
        if not isinstance(new_precision, int):
            raise TypeError("Precision must be an integer.")
        if new_precision < 0:
            raise ValueError("Precision cannot be negative.")
        self.__precision = new_precision

    def get_level(self):
        return self.__level
    def set_level(self, new_level):
        if not isinstance(new_level, int):
            raise TypeError("Level must be an integer.")
        if new_level < 1:
            raise ValueError("Level must be at least 1.")
        self.stats_calculation(self.get_level(), new_level)
        self.__level = new_level

    def get_exp(self):
        return self.__exp
    def set_exp(self, new_exp):
        if not isinstance(new_exp, int):
            raise TypeError("Exp must be an integer.")
        if new_exp < 0:
            raise ValueError("Exp cannot be negative.")
        self.__exp = new_exp
        self.check_levelup()


    def get_types(self):
        return self.__types
    def set_types(self, new_types):
        if not isinstance(new_types, list):
            raise TypeError("Types must be a list.")
        if not all(isinstance(t, PokemonType) for t in new_types):
            raise ValueError("Each type must be a Type object.")
        if len(new_types) == 0:
            raise ValueError("A Pokémon must have at least one type.")
        self.__types = new_types


    def get_can_evolve(self):
        return self.__can_evolve
    def set_can_evolve(self, new_can_evolve):
        if not isinstance(new_can_evolve, bool):
            raise TypeError("Exp must be a boolean.")
        self.__can_evolve = new_can_evolve

    def get_evolution_level(self):
        return self.__evolution_level
    def set_evolution_level(self, new_evolution_level):
        if not isinstance(new_evolution_level, int):
            raise TypeError("Evolution Level must be an integer.")
        if new_evolution_level < 0:
            raise ValueError("Evolution Level cannot be negative.")
        self.__evolution_level = new_evolution_level
        self.check_evolution()

    def get_evolution_pokemon(self):
        return self.__evolution_pokemon
    def set_evolution_pokemon(self, new_evolution_pokemon):
        if not isinstance(new_evolution_pokemon, list):
            raise TypeError("Evolution Pokemon must be a list.")
        if not all(isinstance(t, str) for t in new_evolution_pokemon):
            raise ValueError("Each evolution must be a Str object.")
        self.__evolution_pokemon = new_evolution_pokemon


    # End of getters and setters ----------------------------------------------------------------------------------------

    # Level-related methods ---------------------------------------------------------------------------------------------

    def check_levelup(self):
        required_exp = pow(1.03,2*self.__level) + self.__level + 31
        if self.__exp > required_exp:
            self.set_exp(self.__exp - required_exp)
            self.set_level(self.__level + 1)
            self.check_levelup()


    def stats_calculation(self, original_level, new_level):
        for loop in range(original_level,new_level):
            self.set_max_hp(self.__max_hp + self.__hp//50)
            self.set_hp(self.get_max_hp())
            self.set_attack(self.__attack + self.__attack//50)
            self.set_defense(self.__defense + self.__defense//50)
            self.set_speed(self.__speed + self.__speed//50)
        self.check_evolution()

def check_evolution(self):

    from scripts.logic.json_management import filter_pokemons_by_ids, load_types_from_json

    # Check if evolution is possible
    if not self.get_can_evolve():
        return
    
    if self.get_level() < self.get_evolution_level():
        return

    # Load types
    type_dict = load_types_from_json("assets/data/types.json")

    # Get possible evolutions IDs
    evolution_ids = self.get_evolution_pokemon()

    # Create the matching Pokémons
    candidates = filter_pokemons_by_ids(evolution_ids, type_dict)

    # Chose a Pokémon
    new_pokemon = random.choice(candidates)

    # Appliquer l'évolution
    self.set_id(new_pokemon.get_id())
    self.set_name(new_pokemon.get_name())
    self.set_max_hp(new_pokemon.get_max_hp())
    self.set_hp(new_pokemon.get_max_hp())
    self.set_attack(new_pokemon.get_attack())
    self.set_defense(new_pokemon.get_defense())
    self.set_speed(new_pokemon.get_speed())
    self.set_precision(new_pokemon.get_precision())
    self.set_can_evolve(new_pokemon.get_can_evolve())
    self.set_evolution_level(new_pokemon.get_evolution_level())
    self.set_evolution_pokemon(new_pokemon.get_evolution_pokemon())

    # Recalcul des stats
    self.stats_calculation(1, self.get_max_hp())

        

