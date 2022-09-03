from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid) - 2
        n = len(grid[0]) - 2
        result = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = max(max(grid[i][j: j+3]), max(grid[i+1][j:j+3]), max(grid[i+2][j:j+3]))
        return result


