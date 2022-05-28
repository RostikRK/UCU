"""Furniture"""
class Furniture:
    """
    Main Furniture
    """
    def __init__(self, style, assign):
        """
        Adding attributes to a class
        >>> furn1 = Furniture("asdf", "djss")
        >>> print(furn1.style)
        asdf
        """
        self.style = style
        self.assign = assign
    def __str__(self):
        """
        Defines what we display when print object
        >>> furn1 = Furniture("asdf", "djss")
        >>> print(furn1)
        <furniture style is asdf>
        """
        return f"<furniture style is {self.style}>"

class Chair(Furniture):
    """
    Main chair
    """
    def __init__(self, style, assign, tipe):
        """
        Adding attributes to a class
        >>> charr1 = Chair("djsd", "ksor", "spaj")
        >>> print(charr1.style)
        djsd
        """
        super().__init__(style, assign)
        self.tipe = tipe
    def get_assign(self):
        """
        Defines and displays an assign
        >>> charr1 = Chair("djsd", "ksor", "spaj")
        >>> print(charr1.get_assign())
        ksor
        """
        return self.assign
    def __str__(self):
        """
        Defines what we display when print
        >>> charr1 = Chair("djsd", "ksor", "spaj")
        >>> print(charr1)
        <This spaj furniture style is djsd>
        """
        return f"<This {self.tipe} furniture style is {self.style}>"
        