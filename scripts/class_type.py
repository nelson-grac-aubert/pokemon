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
        self.__negate = negates