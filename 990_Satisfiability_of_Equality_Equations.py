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
    def equationsPossible(self, equations: List[str]) -> bool:
        wuf = WeightedUnionFind(26)
        not_equal_pair = []
        for eq in equations:
            v1 = ord(eq[0]) - ord("a")
            v2 = ord(eq[3]) - ord("a")
            if eq[1:3] == "==":
                wuf.union(v1, v2)
            else:
                if wuf.find(v1) == wuf.find(v2):
                    return False
                else:
                    not_equal_pair.append([v1, v2])
        for nep in not_equal_pair:
            if wuf.find(nep[0]) == wuf.find(nep[1]):
                return False
        return True