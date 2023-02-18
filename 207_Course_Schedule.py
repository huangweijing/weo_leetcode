from typing import List

class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for _ in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int):
        self.vertex_adj_list[v1].append(v2)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]


class Solution:
    def __init__(self):
        self.g = Graph(0)
        self.has_loop = []
        self.path = set[int]()

    def dfs_check_loop(self, node: int) -> bool:
        if self.has_loop[node] is not None:
            return self.has_loop[node]
        if node in self.path:
            self.has_loop[node] = True
            return True
        self.path.add(node)
        adj_list = self.g.get_adjacent_vertex(node)
        for adj_node in adj_list:
            if self.dfs_check_loop(adj_node):
                self.has_loop[node] = True
                return True
        self.path.remove(node)
        self.has_loop[node] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = Graph(numCourses)
        self.has_loop = [None] * numCourses
        self.g = g
        for conn in prerequisites:
            g.add_edge(conn[0], conn[1])
        for node in range(numCourses):
            if self.dfs_check_loop(node):
                return False
        return True


data = [
    2
    , [[1, 0], [0, 1]]
]
r = Solution().canFinish(*data)
print(r)
