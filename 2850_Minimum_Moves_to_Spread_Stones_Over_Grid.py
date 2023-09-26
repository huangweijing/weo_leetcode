from typing import List


class Solution:
    def bfs(self, grid: list[list[int]], r: int, c: int):
        pass


    def minimumMoves(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(grid):
                ans += self.bfs(grid, i, j)
