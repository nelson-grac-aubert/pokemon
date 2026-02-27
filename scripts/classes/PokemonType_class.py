class PokemonType : 
    def __init__(self, name : str, weaknesses : list, strenghts : list, useless : list) : 
        """
        Docstring for __init__
        
        :param name: The name of that Type
        :type name: str
        :param weaknesses: A list of Types against which self is weak
        :type weaknesses: list
        :param strenghts: A list of Types against which self if strong
        :type strenghts: list
        :param useless: A list of Types against which self does 0 damage
        :type useless: list
        """

        self.__name = name
        self.__weaknesses = weaknesses
        self.__strenghts = strenghts
        self.__useless = useless

    # Getters and Setters ---------------------------------------------------------------------------

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string.")
        if new_name.strip() == "":
            raise ValueError("Name cannot be empty.")
        self.__name = new_name

    def get_weaknesses(self) : 
        return self.__weaknesses
    def set_weaknesses(self, new_weaknesses):
        if not isinstance(new_weaknesses, list):
            raise TypeError("Weaknesses must be a list.")
        if not all(isinstance(t, PokemonType) for t in new_weaknesses):
            raise ValueError("Each type must be a Type object.")
        self.__weaknesses = new_weaknesses


    def get_strenghts(self) : 
        return self.__strenghts
    def set_strenghts(self, new_strenghts):
        if not isinstance(new_strenghts, list):
            raise TypeError("strenghts must be a list.")
        if not all(isinstance(t, PokemonType) for t in new_strenghts):
            raise ValueError("Each type must be a Type object.")
        self.__strenghts = new_strenghts

    
    
    def get_useless(self) : 
        return self.__useless
    def set_useless(self, new_useless):
        if not isinstance(new_useless, list):
            raise TypeError("useless must be a list.")
        if not all(isinstance(t, PokemonType) for t in new_useless):
            raise ValueError("Each type must be a Type object.")
        self.__useless = new_useless


    # End of getters and setters ---------------------------------------------------------------------------------------
