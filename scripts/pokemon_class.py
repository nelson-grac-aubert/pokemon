from class_type import Type

class Pokemon : 
    def __init__(self, name : str, hp : int, attack : int, defense : int, types : list, id : str ) : 
        """
        Docstring for __init__
        
        :param name: The name of that Pokemon
        :type name: str
        :param hp: The health points of that Pokemon
        :type hp: int
        :param attack: The attack rating of that Pokemon
        :type attack: int
        :param defense: The defense rating of that Pokemon
        :type defense: int
        :param types: A list of the Types of that Pokemon
        :type types: list
        :param id: The id of that pokemon in a 3 digit format, used to get the sprites files
        :type id: str
        """

        self.__id = id
        self.__name = name
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__level = 1
        self.__types = types 
        
    # Getters and setters -----------------------------------------------------------------------------------------------

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        if new_name.strip() == "":
            raise ValueError("Name cannot be empty.")
        self.__name = new_name

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
            raise ValueError("Attack cannot be negative.")
        self.__attack = new_attack

    def get_defense(self):
        return self.__defense

    def set_defense(self, new_defense):
        if not isinstance(new_defense, int):
            raise TypeError("Defense must be an integer.")
        if new_defense < 0:
            raise ValueError("Defense cannot be negative.")
        self.__defense = new_defense

    def get_level(self):
        return self.__level

    def set_level(self, new_level):
        if not isinstance(new_level, int):
            raise TypeError("Level must be an integer.")
        if new_level < 1:
            raise ValueError("Level must be at least 1.")
        self.__level = new_level

    def get_types(self):
        return self.__types

    def set_types(self, new_types):
        if not isinstance(new_types, list):
            raise TypeError("Types must be a list.")
        if not all(isinstance(t, Type) for t in new_types):
            raise ValueError("Each type must be a Type object.")
        if len(new_types) == 0:
            raise ValueError("A Pokémon must have at least one type.")
        self.__types = new_types

    # End of getters and setters ---------------------------------------------------------------------------------------
