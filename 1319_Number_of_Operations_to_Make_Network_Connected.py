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

    def union(self, p: int, q: int) -> bool:
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return False
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1
        return True


class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        wuf = WeightedUnionFind(n)
        for conn in connections:
            wuf.union(conn[0], conn[1])
        return wuf.count - 1

