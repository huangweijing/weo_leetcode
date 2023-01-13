from typing import List
import math

class WeightedUnionFind:

    def __init__(self, size):
        self.node = [i for i in range(size)]
        self.roads = [math.inf for _ in range(size)]
        self.size = [1] * size
        self.count = size
        pass

    def find(self, p: int):
        while self.node[p] != p:
            p = self.node[p]
        return p

    def union(self, p: int, q: int, road_len: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            self.roads[p] = min(self.roads[p], road_len)
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
            self.roads[q] = min(self.roads[p], self.roads[q], road_len)
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
            self.roads[p] = min(self.roads[p], self.roads[q], road_len)
        self.count -= 1

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        wuf = WeightedUnionFind(n + 1)
        for road in roads:
            wuf.union(road[0], road[1], road[2])
        group = wuf.find(1)
        return wuf.roads[group]

data = [
    4,
    [[1,2,2],[1,3,4],[3,4,7]]
]
r = Solution().minScore(* data)
print(r)
