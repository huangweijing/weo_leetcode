from typing import List
from collections import defaultdict

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
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(lambda : list[int]())
        cols = defaultdict(lambda: list[int]())
        for i, stone in enumerate(stones):
            rows[stone[0]].append(i)
            cols[stone[1]].append(i)
        wuf = WeightedUnionFind(len(stones))
        for row in rows.values():
            for i in range(1, len(row)):
                wuf.union(row[i - 1], row[i])
        for col in cols.values():
            for i in range(1, len(col)):
                wuf.union(col[i - 1], col[i])
        return len(stones) - wuf.count


