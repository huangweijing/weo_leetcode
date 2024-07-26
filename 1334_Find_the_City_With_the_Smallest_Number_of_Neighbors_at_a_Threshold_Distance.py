from typing import List
from sortedcontainers import SortedList
import math


class Graph:
    def __init__(self, n: int) -> None:
        self.n = n
        self.edge_cnt = 0
        self.adjacent_edges = [dict[int, int]() for _ in range(n)]
        self.sp_mat = [[math.inf] * n for _ in range(n)]

    def add_edge(self, v1: int, v2: int, weight: int):
        self.adjacent_edges[v1][v2] = weight
        self.adjacent_edges[v2][v1] = weight
        self.edge_cnt += 1

    def min_dist_all(self):
        for i in range(self.n):
            self.min_dist(i)

    def min_dist(self, s: int):
        visited = set[int]()
        sl = SortedList(key=lambda x: x[1])
        sl.add([s, 0])
        while len(sl) > 0:
            cur = sl.pop(0)
            v, path_len = cur[0], cur[1]
            if v != s:
                self.sp_mat[s][v] = min(path_len, self.sp_mat[s][v])
                self.sp_mat[v][s] = min(path_len, self.sp_mat[v][s])
            for adj, weight in self.adjacent_edges[v].items():
                hash_id = min(v, adj) * 121 + max(v, adj)
                if hash_id not in visited:
                    sl.add([adj, weight + path_len])
                    visited.add(hash_id)
            # print(visited, sl)
        # print(self.sp_mat)

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = Graph(n)
        for edge in edges:
            g.add_edge(*edge)
        g.min_dist_all()
        ans = -1
        min_city_cnt = math.inf
        for i, row in enumerate(g.sp_mat):
            city_cnt = 0
            for val in row:
                if val <= distanceThreshold:
                    city_cnt += 1
            # print(i, city_cnt)
            if city_cnt <= min_city_cnt:
                min_city_cnt = city_cnt
                ans = i
        return ans




data = [
4
, [[0,2,7732],[1,3,7714],[0,1,4106],[0,3,7084]]
, 8439
]
r = Solution().findTheCity(*data)
print(r)