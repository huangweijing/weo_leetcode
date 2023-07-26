from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort(reverse=True)
        ans = 0
        for col_idx in range(len(grid[0])):
            max_val = 0
            for row in grid:
                max_val = max(row[col_idx], max_val)
            ans += max_val
        return ans