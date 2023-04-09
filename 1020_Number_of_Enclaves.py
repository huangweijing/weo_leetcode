from typing import List

class Solution:
    def draw_island(self, grid: List[List[int]]
                    , row: int, col: int) -> (int, bool):
        if grid[row][col] != 1:
            return 0, False
        m, n = len(grid), len(grid[0])
        grid[row][col] = 2
        is_island = True
        land_cnt = 1
        if row == 0 or col == 0 or row == m - 1 or col == n - 1:
            is_island = False
        if row > 0 and grid[row - 1][col] == 1:
            sub_land_cnt, sub_is_island = self.draw_island(grid, row - 1, col)
            is_island &= sub_is_island
            land_cnt += sub_land_cnt
        if row < m - 1 and grid[row + 1][col] == 1:
            sub_land_cnt, sub_is_island = self.draw_island(grid, row + 1, col)
            is_island &= sub_is_island
            land_cnt += sub_land_cnt
        if col > 0 and grid[row][col - 1] == 1:
            sub_land_cnt, sub_is_island = self.draw_island(grid, row, col - 1)
            is_island &= sub_is_island
            land_cnt += sub_land_cnt
        if col < n - 1 and grid[row][col + 1] == 1:
            sub_land_cnt, sub_is_island = self.draw_island(grid, row, col + 1)
            is_island &= sub_is_island
            land_cnt += sub_land_cnt
        return land_cnt, is_island

    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    land_cnt, is_island = self.draw_island(grid, i, j)
                    ans += land_cnt if is_island else 0
        return ans