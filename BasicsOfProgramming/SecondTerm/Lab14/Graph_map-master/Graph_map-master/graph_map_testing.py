from unittest import TestCase, main
import dfs
import bfs
from topological_sort import topological_sort
import graph


class Graph_Test(TestCase):
    def read_file(self, path):
        g = graph.Graph(directed=True)
        vertexes = []
        edges = []
        with open(path, "r") as file:
            for line in file.readlines():
                if line.startswith("#"):
                    None
                else:
                    temp = list(line.split(" "))
                    vertexes.append(temp[0])
                    for word in temp[1:]:
                        res_word = ""
                        for char in word:
                            if char not in ",()\n":
                                res_word += char
                        if res_word == "none":
                            None
                        else:
                            edges.append((temp[0], res_word))
        for vert in vertexes:
            g.insert_vertex(vert)
        for edge in edges:
            g.insert_edge(g.get_vertex(edge[0]), g.get_vertex(edge[1]), None)
        return g

    def test_bts(self):
        gra = self.read_file("Stanford_cs.txt")
        u = gra.get_vertex("CS161")
        result = {u.element(): None}
        self.assertEqual(list(bfs.BFS(gra, u, result).keys()), [
                         'CS161', 'CS109', 'CS106B', 'CS103', 'CS106A'])
        e = gra.get_vertex("MATH53")
        result2 = {e.element(): None}
        self.assertEqual(list(bfs.BFS(gra, e, result2).keys()), [
                         'MATH53', 'MATH51', 'MATH21', 'MATH20', 'MATH19'])
        self.assertEqual(list(bfs.BFS_complete(gra).keys()), ['MATH19', 'MATH20', 'MATH21', 'MATH51', 'CS108', 'CS161', 'CS109', 'CS106B', 'CS103',
                         'CS106A', 'PHYS21', 'PHYS23', 'CS194W', 'CS221', 'CS155', 'CS110', 'CS107', 'CS145', 'CS154', 'CS148', 'CS144', 'ENGR40M', 'MATH52', 'MATH53'])

    def test_dfs(self):
        gra = self.read_file("Stanford_cs.txt")
        u = gra.get_vertex("CS161")
        result = {u.element(): None}
        self.assertEqual(list(dfs.DFS(gra, u, result).keys()), [
                         'CS161', 'CS109', 'CS106B', 'CS106A', 'CS103'])
        e = gra.get_vertex("MATH53")
        result2 = {e.element(): None}
        self.assertEqual(list(dfs.DFS(gra, e, result2).keys()), [
                         'MATH53', 'MATH51', 'MATH21', 'MATH20', 'MATH19'])
        self.assertEqual(list(dfs.DFS_complete(gra).keys()), ['MATH19', 'MATH20', 'MATH21', 'MATH51', 'CS108', 'CS161', 'CS109', 'CS106B', 'CS106A',
                         'CS103', 'PHYS21', 'PHYS23', 'CS194W', 'CS221', 'CS155', 'CS110', 'CS107', 'CS145', 'CS154', 'CS148', 'CS144', 'ENGR40M', 'MATH52', 'MATH53'])

    def test_topological_sort(self):
        gra = self.read_file("Stanford_cs.txt")
        self.assertEqual(topological_sort(gra), ['MATH53', 'MATH52', 'MATH51', 'MATH21', 'MATH20', 'MATH19', 'ENGR40M', 'PHYS23', 'PHYS21', 'CS144',
                         'CS148', 'CS154', 'CS145', 'CS155', 'CS110', 'CS107', 'CS221', 'CS194W', 'CS108', 'CS161', 'CS109', 'CS103', 'CS106B', 'CS106A'])


if __name__ == "__main__":
    main()
