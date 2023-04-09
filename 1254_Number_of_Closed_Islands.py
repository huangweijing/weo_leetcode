from typing import List


class Solution:
    def draw_island(self, grid: List[List[int]]
                    , row: int, col: int) -> bool:
        if grid[row][col] != 0:
            return False
        m, n = len(grid), len(grid[0])
        grid[row][col] = 2
        is_island = True
        if row == 0 or col == 0 or row == m - 1 or col == n - 1:
            is_island = False
        if row > 0 and grid[row - 1][col] == 0:
            is_island &= self.draw_island(grid, row - 1, col)
        if row < m - 1 and grid[row + 1][col] == 0:
            is_island &= self.draw_island(grid, row + 1, col)
        if col > 0 and grid[row][col - 1] == 0:
            is_island &= self.draw_island(grid, row, col - 1)
        if col < n - 1 and grid[row][col + 1] == 0:
            is_island &= self.draw_island(grid, row, col + 1)
        return is_island

    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    is_island = self.draw_island(grid, i, j)
                    ans += 1 if is_island else 0
                    # print(i, j, is_island, grid)
        return ans

data = [[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
r = Solution().closedIsland(data)
print(r)