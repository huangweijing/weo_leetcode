import math
from typing import List
from functools import cache

class Graph:
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

class Solution:
    def __init__(self):
        self.searched_mark = []
        self.price = []
        self.g = Graph(0)

    @cache
    def get_cost(self, last: int, start_vertex: int, end_vertex: int) -> int:
        self.searched_mark[start_vertex] = 1
        if start_vertex == end_vertex:
            return self.price[start_vertex]

        ans = math.inf
        adj_vertex_list = self.g.get_adjacent_vertex(start_vertex)
        for adj_vertex in adj_vertex_list:
            if last == adj_vertex:
                continue
            cost = self.get_cost(start_vertex, adj_vertex, end_vertex)
            ans = min(cost + self.price[start_vertex], ans)

        return ans

    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        self.g = Graph(n)
        self.searched_mark = [0] * n
        self.price = price
        for edge in edges:
            self.g.add_edge(edge[0], edge[1])
        # degree1
        degree1_set = set()
        degree1_parent_set = set()
        for i in range(n):
            if len(self.g.get_adjacent_vertex(i)) == 1:
                degree1_set.add(i)
                degree1_parent_set.add(self.g.get_adjacent_vertex(i)[0])
        ans = 0
        for n1 in degree1_set:
            for n2 in degree1_parent_set:
                cost = self.get_cost(None, n1, n2)
                if cost > ans:
                    ans = cost
                    # print(n1, n2, cost)
        return ans

data = [
    3
    , [[0, 1], [1, 2]]
    , [1,1,1]
]
s = Solution()
r = s.maxOutput(* data)
print(r)