from typing import List


class Solution:
    def __init__(self):
        self.grid = []
        self.visited = []

    def dfs(self, i: int, j: int):
        if i < 0 or i >= len(self.grid):
            return 0
        if j < 0 or j >= len(self.grid[0]):
            return 0
        if self.visited[i][j] == 1 or self.grid[i][j] == 0:
            return 0
        fish_val = self.grid[i][j]
        self.visited[i][j] = 1
        fish_val += self.dfs(i - 1, j)
        fish_val += self.dfs(i + 1, j)
        fish_val += self.dfs(i, j - 1)
        fish_val += self.dfs(i, j + 1)
        return fish_val

    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.grid = grid
        m, n = len(self.grid), len(self.grid[0])
        self.visited = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if self.visited[i][j] == 1 or self.grid[i][j] == 0:
                    continue
                ans = max(ans, self.dfs(i, j))
        return ans
