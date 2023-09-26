import math
from typing import List

class Edge:
    def __init__(self, v: int, w: int, weight: float):
        self.v = v
        self.w = w
        self.weight = weight


class Graph:
    def __init__(self, vertex_count: int):
        self.vertex_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int, weight: float):
        edge = Edge(v1, v2, weight)
        self.vertex_adj_list[v1].append(edge)
        self.vertex_adj_list[v2].append(edge)
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_vertex(self, v) -> list[int]:
        return self.vertex_adj_list[v]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = Graph(len(points))
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                dis = math.sqrt(p1[0] * p1[0] + p2[0] * p2[0])
                graph.add_edge(i, j, dis)
        


