from collections import List

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
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        wuf = WeightedUnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if j > 0 and grid[i][j - 1] == "1":
                    wuf.union(i * n + j, i * n + j - 1)
                if i > 0 and grid[i - 1][j] == "1":
                    wuf.union(i * n + j, (i - 1) * n + j)
        island_set = set[int]()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island_id = wuf.find(i * n + j)
                    island_set.add(island_id)
        return len(island_set)




