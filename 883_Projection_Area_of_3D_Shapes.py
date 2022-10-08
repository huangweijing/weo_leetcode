from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        area = 0
        for row in grid:
            area += max(row)

        for col_idx in range(n):
            col_max = 0
            for row_idx in range(n):
                col_max = max(col_max, grid[row_idx][col_idx])
                if grid[row_idx][col_idx] != 0:
                    area += 1
            area += col_max
        return area