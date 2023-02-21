
class Graph:
    def __init__(self, vertex_count: int):
        self.out_vertex_adj_list = [[] for _ in range(vertex_count)]
        self.in_vertex_adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.out_vertex_adj_list[v1].append(v2)
        self.in_vertex_adj_list[v2].append(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_out_adjacent_vertex(self, v) -> list[int]:
        return self.out_vertex_adj_list[v]

    def get_in_adjacent_vertex(self, v) -> list[int]:
        return self.in_vertex_adj_list[v]

g = DirectedGraphList(5)
g.add_edge(3, 4)
g.add_edge(4, 7)
print(g.get_out_adjacent_vertex(4))