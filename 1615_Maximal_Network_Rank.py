from typing import List


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [set[int]() for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

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


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = Graph(n)
        for road in roads:
            g.add_edge(road[0], road[1])
        ans = 0
        for v in range(g.vertex_count):
            for v2 in range(g.vertex_count):
                if v == v2:
                    continue
                rank = len(g.get_adjacent_vertex(v2)) + len(g.get_adjacent_vertex(v))
                if v2 in g.get_adjacent_vertex(v):
                    rank -= 1
                ans = max(rank, ans)
        return ans
