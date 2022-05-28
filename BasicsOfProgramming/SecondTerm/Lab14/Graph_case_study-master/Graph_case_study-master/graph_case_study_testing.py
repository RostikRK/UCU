from unittest import TestCase, main
import algorithms
import graph


class Graph_Test(TestCase):
    def read_file(self, path):
        g = graph.LinkedDirectedGraph()
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
            g.addVertex(vert)
        for edge in edges:
            g.addEdge(edge[0], edge[1], None)
        return g

    def test_bts(self):
        g = self.read_file("Stanford_cs.txt")
        self.assertEqual(algorithms.bfs(g, g.getVertex("CS148")), [
                         'CS148', 'CS110', 'CS107', 'CS106B', 'CS106A'])
        self.assertEqual(algorithms.bfs(g, g.getVertex("CS161")), [
                         'CS161', 'CS109', 'CS106B', 'CS103', 'CS106A'])

    def test_dfs(self):
        g = self.read_file("Stanford_cs.txt")
        self.assertEqual(algorithms.dfs(g, g.getVertex("CS148")), [
                         'CS110', 'CS107', 'CS106B', 'CS106A', 'CS148'])
        self.assertEqual(algorithms.dfs(g, g.getVertex("MATH21")), [
                         'MATH20', 'MATH19', 'MATH21'])

    def test_topological_sort(self):
        g = self.read_file("Stanford_cs.txt")
        self.assertEqual(algorithms.topological_sort(g), ['MATH53', 'MATH52', 'ENGR40M', 'CS144', 'CS148', 'CS154', 'CS145', 'CS155', 'CS110', 'CS107',
                         'CS221', 'CS194W', 'PHYS23', 'PHYS21', 'CS108', 'CS161', 'CS109', 'CS103', 'CS106B', 'CS106A', 'MATH51', 'MATH21', 'MATH20', 'MATH19'])


if __name__ == "__main__":
    main()
