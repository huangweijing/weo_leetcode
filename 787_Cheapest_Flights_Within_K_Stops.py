from typing import List
from collections import deque
import math
from functools import cache

class Edge:
    def __init__(self, src: int, dst: int, cost: int):
        self.cost = cost
        self.src = src
        self.dst = dst

class Graph:
    def __init__(self, vertex_count: int):
        self.edge_adj_list = [[] for x in range(vertex_count)]
        self.edge_count = 0
        self.vertex_count = vertex_count

    def add_edge(self, v1: int, v2: int, cost: int):
        self.edge_adj_list[v1].append(Edge(v1, v2, cost))
        self.edge_count += 1

    def get_vertex_count(self) -> int:
        return self.vertex_count

    def get_edge_count(self) -> int:
        return self.edge_count

    def get_adjacent_edge(self, v) -> list[Edge]:
        return self.edge_adj_list[v]

class Solution:
    def __init__(self):
        self.n = 0
        self.g: Graph = Graph(1)

    @cache
    def my_sol(self, src: int, dst: int, k: int) -> int:
        # print(src, dst, k)
        if k < 0 or (k == 0 and src != dst):
            return None
        if src == dst:
            return 0
        edge_list = self.g.get_adjacent_edge(src)
        ans = math.inf
        for edge in edge_list:
            sub = self.my_sol(edge.dst, dst, k - 1)
            if sub is not None:
                ans = min(ans, edge.cost + sub)
        return ans

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.n = n
        self.g = Graph(n)
        for flight in flights:
            self.g.add_edge(flight[0], flight[1], flight[2])
        ans = self.my_sol(src, dst, k + 1)
        if ans == math.inf:
            return -1
        return ans

data = [
    5
    , [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
    , 2
    , 1
    , 1
]
r = Solution().findCheapestPrice(* data)
print(r)

