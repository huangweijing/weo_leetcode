class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cell_cnt = 0
        adj_cell_cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cell_cnt += 1
                    if i > 0 and grid[i - 1][j] == 1:
                        adj_cell_cnt += 1
                    if j > 0 and grid[i][j - 1] == 1:
                        adj_cell_cnt += 1
        return cell_cnt * 4 - adj_cell_cnt * 2

