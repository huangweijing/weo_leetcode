from typing import List
from collections import Counter
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
        self.g = Graph(1)
        self.labels = []
        self.ans = []

    # @cache
    def my_sol(self, parent: int, root:int) -> Counter:
        adj_vertex_list = self.g.get_adjacent_vertex(root)
        cnt = Counter()
        cnt[self.labels[root]] += 1
        for v in adj_vertex_list:
            if v != parent:
                sub_cnt = self.my_sol(root, v)
                cnt += sub_cnt
        self.ans[root] = cnt[self.labels[root]]
        return cnt

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.g = Graph(n)
        self.labels = labels
        self.ans = [0] * n
        for edge in edges:
            self.g.add_edge(edge[0], edge[1])
        self.my_sol(None, 0)
        return self.ans

data = [
    7
    , [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
    , "abaedcd"
]
r = Solution().countSubTrees(* data)
print(r)

