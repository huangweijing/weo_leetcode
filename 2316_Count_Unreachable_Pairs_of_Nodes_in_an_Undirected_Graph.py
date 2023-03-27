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
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        wuf = WeightedUnionFind(n)
        for edge in edges:
            wuf.union(edge[0], edge[1])

        part_sizes = dict[int, int]()
        for node, p in enumerate(wuf.node):
            if node == p:
                part_sizes[p] = wuf.size[p]
        ans = 0
        for part_size in part_sizes.values():
            ans += (n - part_size) * part_size
        return ans >> 1

data = [
    11
    , [[5, 0], [1, 0], [10, 7], [9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]
]

r = Solution().countPairs(* data)
print(r)