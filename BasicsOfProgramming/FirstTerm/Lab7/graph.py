"""
Yakas fignya
"""
def get_graph_from_file(file_name):
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    edges = []
    one_edge = []
    with open( file_name, 'r' ) as file:
        for line in file:
            for i in line:
                if i.isnumeric() == True:
                    i = int(i)
                    one_edge.append(i)
                elif i.isnumeric() == False:
                    None
            edges.append(one_edge)
            one_edge = []
    return edges

def to_edge_dict(edge_list):
    """ 
    (list) -> (dict)
    Convert a graph from list of edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    edgedic = {}
    edgeset = set()
    for en in edge_list:
        for jey in en:
            edgeset.add(jey)
    arclist = list(edgeset)
    for j in arclist:
        nonlist =[]
        for i in edge_list:
            if i[0] == j:
                nonlist.append(i[1])
            elif i[1] == j:
                nonlist.append(i[0])
        edgedic[j] = nonlist
    return edgedic


def is_edge_in_graph(graph, edge):
    """ 
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    bylean = False
    for k,v in graph.items():
        for g in v:
            if k == edge[0] and g == edge[1]:
                bylean = True
    return bylean

def add_edge(graph, edge):
    """ 
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    preset = set()
    for k,v in graph.items():
        for g in v:
            preset.add((k, g))
    prelist = list(preset)
    temp = [tuple(sorted(sub)) for sub in prelist]
    normlist = list(set(temp))
    normlist.append(edge)
    finallist = []
    for ing in normlist:
        ing = list(ing)
        finallist.append(ing)
    finaldict = to_edge_dict(finallist)
    return finaldict


def del_edge(graph, edge):
    """ 
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    preset = set()
    for k,v in graph.items():
        for g in v:
            preset.add((k, g))
    prelist = list(preset)
    temp = [tuple(sorted(sub)) for sub in prelist]
    normlist = list(set(temp))
    for jet in normlist:
        if jet == edge:
            normlist.remove(edge)
        else:
            None
    finallist = []
    for ing in normlist:
        ing = list(ing)
        finallist.append(ing)
    finaldict = to_edge_dict(finallist)
    return finaldict


def add_node(graph, node):
    """ 
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    preset = set()
    for k,v in graph.items():
        for g in v:
            preset.add((k, g))
    prelist = list(preset)
    temp = [tuple(sorted(sub)) for sub in prelist]
    normlist = list(set(temp))
    finallist = []
    for ing in normlist:
        ing = list(ing)
        finallist.append(ing)
    edgedic = {}
    edgeset = set()
    for en in finallist:
        for jey in en:
            edgeset.add(jey)
    arclist = list(edgeset)
    arclist.append(node)
    for j in arclist:
        nonlist =[]
        for i in finallist:
            if i[0] == j:
                nonlist.append(i[1])
            elif i[1] == j:
                nonlist.append(i[0])
        edgedic[j] = nonlist
    return edgedic

def del_node(graph, node):
    """ 
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    preset = set()
    for k,v in graph.items():
        for g in v:
            preset.add((k, g))
    prelist = list(preset)
    temp = [tuple(sorted(sub)) for sub in prelist]
    normlist = list(set(temp))
    finallist = []
    for ing in normlist:
        ing = list(ing)
        finallist.append(ing)
    edgedic = {}
    edgeset = set()
    for en in finallist:
        for jey in en:
            edgeset.add(jey)
    arclist = list(edgeset)
    for jet in arclist:
        if jet == node:
            arclist.remove(node)
        else:
            None
    for j in arclist:
        nonlist =[]
        for i in finallist:
            if i[0] == j and i[1] != node:
                nonlist.append(i[1])
            elif i[1] == j and i[0] != node:
                nonlist.append(i[0])
        edgedic[j] = nonlist
    return edgedic


def convert_to_dot(graph):
    """ 
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    >>> 3==7
    False
    """
    pass
