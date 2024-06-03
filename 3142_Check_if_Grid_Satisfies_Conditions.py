from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i > 0 and grid[i - 1][j] != val:
                    return False
                if j > 0 and grid[i][j - 1] == val:
                    return False
        return True

