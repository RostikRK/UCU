"""
Coollllll
"""
def names_read(file_name):
    """
    (str) -> (list)
    Reads the names from file and return a list of names

    >>> ":)" != ";("
    True
    """
    list_of_names = []
    with open( file_name, 'r' ) as file:
        for line in file:
            list_of_names.append(line[:-1])
    return list_of_names



def common_names(female_names, male_names):
    """
    (list, list) -> set
    Compares the names from 2 lists which starts with vowel

    >>> common_names(['Adda', 'Stone', 'Olivia'], ['Mender', 'Olivia'])
    {'Olivia'}
    """
    femtrue = set()
    maltrue = set()
    for ner in female_names:
        if ner.startswith("A") or ner.startswith("E") or ner.startswith("I") or\
ner.startswith("O") or ner.startswith("U") == True:
            femtrue.add(ner)
    for net in male_names:
        if net.startswith("A") or net.startswith("E") or net.startswith("I") or\
net.startswith("O") or net.startswith("U") == True:
            maltrue.add(net)
    res = femtrue.intersection(maltrue)
    return res
