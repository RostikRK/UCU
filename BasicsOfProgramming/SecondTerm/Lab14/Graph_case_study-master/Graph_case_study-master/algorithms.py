"""
File: algorithms.py

Graph processing algorithms
"""

import queue
from linkedstack import LinkedStack
import graph


def topological_sort_rec(g, v, stack):

    # Mark the current node as visited.
    v.setMark()

    # Recur for all the vertices adjacent to this vertex
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            topological_sort_rec(g, w, stack)

    # Push current vertex to stack which stores result
    stack.insert(0, v.getLabel())


def topological_sort(g):
    # Mark all the vertices as not visited
    g.clearVertexMarks()
    stack = []

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for v in g.vertices():
        if not v.isMarked():
            topological_sort_rec(g, v, stack)
    return stack


def dfs(g: graph.LinkedDirectedGraph(), v, stack=LinkedStack()):
    g.clearVertexMarks()
    if isinstance(v, str):
        v = g.getVertex(v)
    v.setMark()
    res = []
    stack.push(v)
    while stack.isEmpty() is False:
        for w in g.neighboringVertices(v.getLabel()):
            if not w.isMarked():
                w.setMark()
                stack.push(w)
        temp = stack.pop()
        res.append(temp.getLabel())
        v = temp
    return res


def bfs(g: graph.LinkedDirectedGraph(), v):
    g.clearVertexMarks()
    if isinstance(v, str):
        v = g.getVertex(v)
    v.setMark()
    res = []
    queue = [v]
    while True:
        for w in g.neighboringVertices(v.getLabel()):
            if not w.isMarked():
                w.setMark()
                queue.append(w)
        try:
            temp = queue.pop(0)
            res.append(temp.getLabel())
            v = temp
        except IndexError:
            break
    return res
