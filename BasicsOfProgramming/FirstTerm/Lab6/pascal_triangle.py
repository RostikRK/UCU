"""
high level support for doing this and that.
"""

def generate_pascal_triangle(numb):
    """
    Creates the pascal triangle as a list
    >>> generate_pascal_triangle(10.2)
    []
    >>> generate_pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if (isinstance(numb, int) == True) and numb>0:
        list = [1]
        res = []
        for elem in range(numb):
            elem = elem
            res.append(list)
            newlist=[]
            newlist.append(list[0])
            for inter in range(len(list)-1):
                newlist.append(list[inter]+list[inter+1])
            newlist.append(list[-1])
            list=newlist
    else:
        res = []
    return res
    