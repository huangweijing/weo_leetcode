from typing import List
from collections import deque

class UndirectedGraph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
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


class AlgorithmGetPathToBFS:
    def __init__(self, g: UndirectedGraph):
        self.graph = g
        self.searched_mark = [0] * self.graph.get_vertex_count()
        self.edge_to = [0] * self.graph.get_vertex_count()

    def get_path_to(self, start_vertex: int, end_vertex: int) -> list[int]:
        self.searched_mark = [0] * self.graph.get_vertex_count()
        self.edge_to = [-1] * self.graph.get_vertex_count()
        self.searched_mark[start_vertex] = 1
        vertex_list = deque()
        vertex_list.append(start_vertex)

        while len(vertex_list) != 0:
            # print(vertex_list, self.edge_to)
            vertex = vertex_list.popleft()
            adj_vertex_list = self.graph.get_adjacent_vertex(vertex)
            for next_vertex in adj_vertex_list:
                if self.searched_mark[next_vertex] == 0:
                    self.searched_mark[next_vertex] = 1
                    self.edge_to[next_vertex] = vertex
                    vertex_list.append(next_vertex)
        if self.edge_to[end_vertex] == -1:
            return []

        path_vertex = end_vertex
        path = deque()
        path.appendleft(path_vertex)
        while path_vertex != start_vertex:
            path_vertex = self.edge_to[path_vertex]
            path.appendleft(path_vertex)

        return list(path)


class Solution:
    def is_connected(self, gene1: str, gene2: str) -> bool:
        diff = 0
        for i, ch in enumerate(gene1):
            if ch != gene2[i]:
                diff += 1
            if diff > 1:
                return False
        if diff == 1:
            return True


    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # print(self.is_connected(start, end))

        g = UndirectedGraph(len(bank) + 1)
        start_vertex, end_vertex = 0, -1
        for i, gene1 in enumerate(bank):
            if gene1 == end:
                end_vertex = i + 1
            if self.is_connected(start, gene1):
                g.add_edge(0, i + 1)
            for j in range(i + 1, len(bank)):
                gene2 = bank[j]
                if i == j:
                    continue
                if self.is_connected(gene1, gene2):
                    g.add_edge(i + 1, j + 1)
        # print(g.vertex_adj_list)
        agp = AlgorithmGetPathToBFS(g)
        path = agp.get_path_to(start_vertex, end_vertex)
        # print(path)
        return len(path) - 1

data = [
"AAAAACCC"
, "AACCCCCC"
, ["AAAACCCC","AAACCCCC","AACCCCCC"]
]
r = Solution().minMutation(* data)
print(r)
