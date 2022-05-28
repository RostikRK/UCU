"""
Recursion
"""


def create_table(rows, colum, lst = None):
    """
    Return the sum table in list of lists
    >>> create_table(4,6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    """
    if lst == None:
        lst = []
    temp_list = []
    k = 0
    for k in range(0, colum):
        if k == 0 or len(lst) == 0:
            temp_list.append(1)
        else:
            temp_list.append(temp_list[-1] + lst[-1][k])

    lst.append(temp_list)
    if len(lst) == rows:
        return lst
    else:
        return create_table(rows, colum, lst)

def flatten(lst):
    """
    Returns one flatten list from list of lists
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    """
    if type(lst) != list:
        return str(lst) + " (not a list)"
    if len(lst) == 0:
        return lst
    elif type(lst[0]) == list:
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return lst[:1] + flatten(lst[1:])
