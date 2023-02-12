class Graph:
    def __init__(self, vertex_count: int):
        pass

    def add_edge(self, v1: int, v2: int):
        pass

    def get_vertex_count(self) -> int:
        pass

    def get_edge_count(self) -> int:
        pass

    def get_adjacent_vertex(self, v) -> list[int]:
        pass

    def calc_degree(self, v) -> int:
        return len(self.get_adjacent_vertex(v))

    def calc_max_degree(self) -> int:
        degree_list = map(self.calc_degree, range(self.get_vertex_count()))
        return max(degree_list)

    def calc_avg_degree(self):
        degree_list = map(self.calc_degree, range(self.get_vertex_count()))
        return max(degree_list) / len(degree_list)
