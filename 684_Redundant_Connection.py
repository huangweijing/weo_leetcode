from typing import List

class WeightedUnionFind:

    def __init__(self, size):
        self.node = [i for i in range(size)]
        self.size = [1] * size
        self.count = size
        pass

    def find(self, p: int):
        while self.node[p] != p:
            p = self.node[p]
        return p

    def union(self, p: int, q: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = []
        wuf = WeightedUnionFind(len(edges))
        for edge in edges:
            bfr_cnt = wuf.count
            wuf.union(edge[0] - 1, edge[1] - 1)
            aft_cnt = wuf.count
            if bfr_cnt == aft_cnt:
                ans = edge
        return ans
