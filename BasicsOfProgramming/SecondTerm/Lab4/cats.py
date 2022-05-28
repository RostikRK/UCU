"""Animals"""
class Animal:
    """
    Main animals
    """
    def __init__(self, phylum, clas):
        """
        Adding attributes to a class
        >>> anim1 = Animal("andk", "asdjs")
        >>> print(anim1.clas)
        asdjs
        """
        self.phylum = phylum
        self.clas = clas
    def __str__(self):
        """
        Defines what to print
        >>> anim1 = Animal("andk", "asdjs")
        >>> print(anim1)
        <animal class is asdjs>
        """
        return f"<animal class is {self.clas}>"

class Cat(Animal):
    """
    Main Cat
    """
    def __init__(self, phylum, clas, genus):
        """
        Adding attributes to a class
        >>> cat1 = Cat("sdfsd", "sdfg", "orue")
        >>> print(cat1.clas)
        sdfg
        """
        super().__init__(phylum, clas)
        self.genus = genus
    def sound(self):
        """
        Adding sound
        >>> cat1 = Cat("sdfsd", "sdfg", "orue")
        >>> print(cat1.sound())
        Meow
        """
        return "Meow"
    def __str__(self):
        """
        Define what we display when print
        >>> cat1 = Cat("sdfsd", "sdfg", "orue")
        >>> print(cat1)
        <This orue animal class is sdfg>
        """
        return f"<This {self.genus} animal class is {self.clas}>"
        