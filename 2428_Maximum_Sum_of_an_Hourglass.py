from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        w, h = len(grid[0]), len(grid)
        max_hg = 0
        for i in range(h - 2):
            for j in range(w - 2):
                hour_glass = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1]\
                    + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                max_hg = max(hour_glass, max_hg)
        return max_hg

