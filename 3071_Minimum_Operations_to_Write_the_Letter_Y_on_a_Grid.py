from typing import List

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        y_cell = [0, 0, 0]
        other_cell = [0, 0, 0]
        n = len(grid)
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                is_y = False
                if i <= n // 2 and i == j:
                    is_y = True
                if i <= n // 2 and i + j == n - 1:
                    is_y = True
                if i >= n // 2 and j == n // 2:
                    is_y = True
                if is_y:
                    y_cell[grid[i][j]] += 1
                else:
                    other_cell[grid[i][j]] += 1
        return min(y_cell[1] + y_cell[2] + other_cell[0] + min(other_cell[1], other_cell[2])
            , y_cell[0] + y_cell[2] + other_cell[1] + min(other_cell[0], other_cell[2])
            , y_cell[0] + y_cell[1] + other_cell[2] + min(other_cell[0], other_cell[1]))


data = [
    [1, 1, 1, 1, 1]
    , [1, 1, 1, 1, 1]
    , [1, 1, 1, 1, 1]
    , [1, 1, 1, 1, 1]
    , [1, 1, 1, 1, 1]
]
r = Solution().minimumOperationsToWriteY(data)
print(r)