""" Bulding """
import classroom
class AcademicBuilding:
    """
    Main building
    """
    def __init__(self, address, classrooms):
        """
        Adding attributes to a class
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building.address)
        Kozelnytska st. 2a
        """
        self.address = address
        self.classrooms = classrooms
    def total_equipment(self):
        """
        Counts the total equipment in the building
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC'])
        >>> classroom_007 = classroom.Classroom('007', 12, [])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC'])
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
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
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
