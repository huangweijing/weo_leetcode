from Graph import Graph


class AlgorithmHasEdgeToDFS:
    def __init__(self, g: Graph):
        self.graph = g
        self.searched_mark = [0] * self.graph.get_vertex_count()

    def has_path_to(self, start_vertex: int, end_vertex: int) -> bool:
        self.searched_mark[start_vertex] = 1
        if start_vertex == end_vertex:
            return True

        adj_vertex_list = self.graph.get_adjacent_vertex(start_vertex)
        print(f"{adj_vertex_list}")
        for adj_vertex in adj_vertex_list:
            if self.searched_mark[adj_vertex]:
                continue
            if self.has_path_to(adj_vertex, end_vertex):
                return True
        return False


