from Graph import Graph


class UndirectedGraphList(Graph):
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]

        print(self.vertex_adj_list)
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.vertex_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]


g = UndirectedGraphList(10)
g.add_edge(3, 5)
g.add_edge(2, 6)
g.add_edge(7, 6)
g.add_edge(7, 5)
g.add_edge(7, 1)
g.add_edge(7, 2)
print(g.get_edge_count())
print(g.get_adjacent_vertex(6))
print(g.calc_degree(6))
print(g.calc_max_degree())