""" Bulding """
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

class Building:
    """
    Main building
    """
    def __init__(self, address):
        """
        Adding attributes to a class
        >>> build1 = Building("The address")
        >>> print(build1.address)
        The address
        """
        self.address = address

class House(Building):
    """
    Main house
    """
    def __init__(self, address, rooms: list):
        """
        Adding attributes to a class
        >>> hous1 = House("The address", [])
        >>> print(hous1.address)
        The address
        """
        super().__init__(address)
        self.rooms = rooms

class AcademicBuilding(Building):
    """
    Main building
    """
    def __init__(self, address, classrooms):
        """
        Adding attributes to a class
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building.address)
        Kozelnytska st. 2a
        """
        super().__init__(address)
        self.classrooms = classrooms
    def total_equipment(self):
        """
        Counts the total equipment in the building
        >>> classroom_016 = Classroom('016', 80, ['PC'])
        >>> classroom_007 = Classroom('007', 12, [])
        >>> classroom_008 = Classroom('008', 25, ['PC'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building.total_equipment())
        [('PC', 2)]
        """
        aleq = [ele for equi in self.classrooms for ele in equi.equipment]
        aleqset = set(aleq)
        res =[(elem, aleq.count(elem)) for elem in aleqset]
        return res
    def __str__(self):
        """
        Finds what to return when we print this class object
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        """
        alls = self.address + "\n"
        for room in self.classrooms:
            alls += str(room) + "\n"
        return alls[:-1]
