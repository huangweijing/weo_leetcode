from Graph import Graph
from collections import deque


class AlgorithmGetPathToBFS:
    def __init__(self, g: Graph):
        self.graph = g
        self.searched_mark = [0] * self.graph.get_vertex_count()
        self.edge_to = [0] * self.graph.get_vertex_count()

    def get_path_to(self, start_vertex: int, end_vertex: int) -> list[int]:
        self.searched_mark = [0] * self.graph.get_vertex_count()
        self.edge_to = [0] * self.graph.get_vertex_count()
        self.searched_mark[start_vertex] = 1
        vertex_list = deque()
        vertex_list.append(start_vertex)

        while len(vertex_list) != 0:
            vertex = vertex_list.popleft()
            adj_vertex_list = self.graph.get_adjacent_vertex(vertex)
            for next_vertex in adj_vertex_list:
                if self.searched_mark[next_vertex] == 0:
                    self.searched_mark[next_vertex] = 1
                    self.edge_to[next_vertex] = vertex
                    vertex_list.append(next_vertex)

        path_vertex = end_vertex
        path = deque()
        path.appendleft(path_vertex)
        while path_vertex != start_vertex:
            path_vertex = self.edge_to[path_vertex]
            path.appendleft(path_vertex)

        return list(path)