from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertex_adj_list = defaultdict(lambda: set[int]())
        self.edge_count = 0
        self.vertex_count = 0

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].add(v2)
        self.vertex_adj_list[v2].add(v1)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> set[int]:
        return self.vertex_adj_list[v]