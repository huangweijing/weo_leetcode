from typing import List
from collections import Counter, defaultdict


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
    def minimumHammingDistance(self, source: List[int], target: List[int]
                               , allowedSwaps: List[List[int]]) -> int:
        ans = 0
        wuf = WeightedUnionFind(len(source))
        group = defaultdict(lambda: Counter())
        for swap in allowedSwaps:
            wuf.union(swap[0], swap[1])
        for i, v in enumerate(source):
            node = wuf.find(i)
            group[node][v] += 1
        for i, v in enumerate(target):
            node = wuf.find(i)
            if group[node][v] > 0:
                group[node][v] -= 1
            else:
                ans += 1
        return ans