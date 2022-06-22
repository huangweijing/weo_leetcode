from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cost_grid = [[0] * n for i in range(m)]
        for row in range(m):
            for col in range(n):
                if row == col == 0:
                    cost_grid[row][col] = grid[row][col]
                elif row == 0:
                    cost_grid[row][col] = cost_grid[row][col - 1] + grid[row][col]
                elif col == 0:
                    cost_grid[row][col] = cost_grid[row - 1][col] + grid[row][col]
                else:
                    cost_grid[row][col] = min(cost_grid[row - 1][col], cost_grid[row][col - 1]) + grid[row][col]

        return cost_grid[m - 1][n - 1]

grid = [[1,2,3],[4,5,6]]
r = Solution().minPathSum(grid)
print(r)