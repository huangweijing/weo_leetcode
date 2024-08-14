from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        row_flip, col_flip = 0, 0
        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][-1-j]:
                    row_flip += 1
        for j in range(n):
            for i in range(m // 2):
                if grid[i][j] != grid[-1-i][j]:
                    col_flip += 1
        return min(row_flip, col_flip)
    

data = [[0,1],[0,1],[0,0]]
r = Solution().minFlips(data)
print(r)