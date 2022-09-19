from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        col_max = []
        row_max = []
        for row in grid:
            col_max.append(max(row))
        for j in range(len(grid[0])):
            max_val = 0
            for i in range(len(grid)):
                max_val = max(grid[i][j], max_val)
            row_max.append(max_val)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += min(col_max[i], row_max[j]) - grid[i][j]
        return result

