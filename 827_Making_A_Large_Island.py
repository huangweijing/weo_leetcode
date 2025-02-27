from typing import List
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.island = []
        self.grid = []

    def dfs(self, ridx, cidx, island_idx: int) -> int:
        self.island[ridx][cidx] = island_idx
        size = 1
        if ridx > 0 and self.grid[ridx - 1][cidx] == 1 and self.island[ridx - 1][cidx] == 0:
            size += self.dfs(ridx - 1, cidx, island_idx)
        if ridx < len(self.grid) - 1 and self.grid[ridx + 1][cidx] == 1 and self.island[ridx + 1][cidx] == 0:
            size += self.dfs(ridx + 1, cidx, island_idx)
        if cidx > 0 and self.grid[ridx][cidx - 1] == 1 and self.island[ridx][cidx - 1] == 0:
            size += self.dfs(ridx, cidx - 1, island_idx)
        if cidx < len(self.grid[0]) - 1 and self.grid[ridx][cidx + 1] == 1 and self.island[ridx][cidx + 1] == 0:
            size += self.dfs(ridx, cidx + 1, island_idx)
        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.island = [[0 for _ in row] for row in grid]
        island_idx = 1
        island_size = Counter()
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val == 1 and self.island[i][j] == 0:
                    size = self.dfs(i, j, island_idx)
                    island_size[island_idx] = size
                    island_idx += 1
                    # print(self.island)
        if len(island_size) == 0:
            return 1
        ans = max(island_size.values())
        # print(island_size)
        for i, row in enumerate(self.island):
            for j, val in enumerate(row):
                if val == 0:
                    part = set()
                    if i > 0:
                        idx = self.island[i - 1][j]
                        size = island_size[idx]
                        part.add((idx, size))
                    if i < len(self.island) - 1:
                        idx = self.island[i + 1][j]
                        size = island_size[idx]
                        part.add((idx, size))
                    if j > 0:
                        idx = self.island[i][j - 1]
                        size = island_size[idx]
                        part.add((idx, size))
                    if j < len(self.island[0]) - 1:
                        idx = self.island[i][j + 1]
                        size = island_size[idx]
                        part.add((idx, size))
                    ans = max(ans, sum([p[1] for p in part]) + 1)
        return ans
    

data = [[1,1],[1,1]]
r = Solution().largestIsland(data)
print(r)
            


        
        
        

