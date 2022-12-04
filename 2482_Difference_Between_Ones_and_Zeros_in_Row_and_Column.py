from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        minus_row, minus_col = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                minus_row[i] += 1 if grid[i][j] == 1 else -1
                minus_col[j] += 1 if grid[i][j] == 1 else -1
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = minus_row[i] + minus_col[j]
        return ans

