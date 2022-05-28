""""Classroom"""
class Classroom:
    """
    Main classroom
    """
    def __init__(self, number, capacity, equipment):
        """
        Adding attributes to a class
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016.capacity)
        80
        """
        self.number = number
        self.capacity = capacity
        self.equipment = equipment
    def __str__(self):
        """
        Finds what to return when we print this class object
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        """
        l_string = ", ".join(self.equipment)
        return f"Classroom {self.number} has a capacity " + \
f"of {self.capacity} persons and has the following equipment: {l_string}."
    def is_larger(first, second):
        """
        Defines which of the triangles is larger
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        return first.capacity>second.capacity
    def equipment_differences(first, second):
        """
        Return an equipment difference between tro classrooms
        >>> classroom_016 = Classroom('016', 80, ['PC'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC']
        """
        return list(set(first.equipment) - set(second.equipment))
    def __repr__(self):
        """
        Finds what to return when we print this class object
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        """
        return "Classroom(%r, %r, %r)" % \
(self.number, self.capacity, self.equipment)
