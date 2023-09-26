from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_axis = (i * n + j + k) % (m * n)
                new_row, new_col = new_axis // n, new_axis % n
                ans[new_row][new_col] = grid[i][j]
        return ans
