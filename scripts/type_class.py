class Type : 
    def __init__(self, name : str, weaknesses : list, strenghts : list, negates : list) : 
        """
        Docstring for __init__
        
        :param name: The name of that Type
        :type name: str
        :param weaknesses: A list of Types against which self is weak
        :type weaknesses: list
        :param strenghts: A list of Types against which self if strong
        :type strenghts: list
        :param negates: A list of Types against which self does 0 damage
        :type negates: list
        """

        self.__name = name
        self.__weaknesses = weaknesses
        self.__strenghts = strenghts
        self.__negates = negates

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
    def set_weaknesses(self, new_weaknesses) :
        if not isinstance(new_weaknesses, list):
            raise TypeError("Weaknesses must be a list.")
        if not all(isinstance(t, Type) for t in new_weaknesses):
            raise ValueError("Each type must be a Type object.")
        if new_weaknesses.strip() == [] : 
            raise ValueError("Weaknesses cannot be empty.")
        self.__weaknesses = new_weaknesses

    
    def get_strenghts(self) : 
        return self.__strenghts
    def set_strenghts(self, new_strenghts) :
        if not isinstance(new_strenghts, list):
            raise TypeError("strenghts must be a list.")
        if not all(isinstance(t, Type) for t in new_strenghts):
            raise ValueError("Each type must be a Type object.")
        if new_strenghts.strip() == [] : 
            raise ValueError("Strenghts cannot be empty.")
        self.__strenghts = new_strenghts
    
    
    def get_negates(self) : 
        return self.__negates
    def set_negates(self, new_negates) :
        if not isinstance(new_negates, list):
            raise TypeError("negates must be a list.")
        if not all(isinstance(t, Type) for t in new_negates):
            raise ValueError("Each type must be a Type object.")
        if new_negates.strip() == [] : 
            raise ValueError("Negates cannot be empty.")
        self.__negates = new_negates

    # End of getters and setters ---------------------------------------------------------------------------------------
