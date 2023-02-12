from Graph import Graph
from AlgorithmHasEdgeToDFS import AlgorithmHasEdgeToDFS
from AlgorithmGetPathToDFS import AlgorithmGetPathToDFS
from AlgorithmGetPathToBFS import AlgorithmGetPathToBFS
from AlgorithmConnectionCheckDFS import AlgorithmConnectionCheckDFS

class UndirectedGraphMatrix(Graph):
    def __init__(self, vertex_count: int):
        self.vertex_matrix = [
            [0 for y in range(vertex_count)] for x in range(vertex_count)
        ]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_matrix[v1][v2] = 1
        self.vertex_matrix[v2][v1] = 1
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        adjacent_vertex = []
        for idx in range(self.vertex_count):
            if self.vertex_matrix[v][idx] == 1:
                adjacent_vertex.append(idx)
        return adjacent_vertex

g = UndirectedGraphMatrix(10)
g.add_edge(4, 9)
g.add_edge(3, 5)
g.add_edge(2, 6)
g.add_edge(7, 6)
g.add_edge(7, 5)
g.add_edge(7, 1)
g.add_edge(7, 2)
g.add_edge(5, 9)
print(g.get_edge_count())
print(g.get_adjacent_vertex(6))
print(g.calc_degree(6))
print(g.calc_max_degree())

alg = AlgorithmHasEdgeToDFS(g)
print(alg.has_path_to(4, 7))

alg = AlgorithmGetPathToDFS(g)
print(alg.get_path_to(3, 6))

alg = AlgorithmGetPathToBFS(g)
print(alg.get_path_to(4, 1))

alg = AlgorithmConnectionCheckDFS(g)
print(f"{alg.get_components_count()}")
print(f"{alg.get_if_connected(1, 4)}")
print(f"{alg.connected_mark}")