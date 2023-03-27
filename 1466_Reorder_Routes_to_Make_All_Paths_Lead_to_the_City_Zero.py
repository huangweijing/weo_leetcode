from typing import List
from collections import defaultdict

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
        self.link_dic = defaultdict(lambda : set[int]())
        self.g = Graph(0)

    def dfs(self, prev: int, cur: int):
        adj_nodes = self.g.get_adjacent_vertex(cur)
        ans = 0
        for node in adj_nodes:
            if node != prev:
                if node in self.link_dic[cur]:
                    ans += 1
                ans += self.dfs(cur, node)
        return ans

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.g = Graph(n)
        for conn in connections:
            self.link_dic[conn[0]].add(conn[1])
            self.g.add_edge(conn[0], conn[1])
        return self.dfs(-1, 0)

data = [
    6
    ,[[0,1],[1,3],[2,3],[4,0],[4,5]]
]
r = Solution().minReorder(* data)
print(r)