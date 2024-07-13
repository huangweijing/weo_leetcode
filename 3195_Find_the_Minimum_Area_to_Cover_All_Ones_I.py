from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row, max_row, min_col, max_col = math.inf, -1, math.inf, -1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        return (max_row - min_row + 1) * (max_col - min_col + 1)

