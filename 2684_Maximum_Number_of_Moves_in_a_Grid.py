from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.grid = []

    @cache
    def my_sol(self, row: int, col: int) -> int:
        val = self.grid[row][col]
        sol1, sol2, sol3 = 0, 0, 0
        if col == len(self.grid[0]) - 1:
            return 1
        if row + 1 < len(self.grid) and self.grid[row + 1][col + 1] > val:
            sol1 = self.my_sol(row + 1, col + 1)
        if self.grid[row][col + 1] > val:
            sol2 = self.my_sol(row, col + 1)
        if row - 1 >= 0 and self.grid[row - 1][col + 1] > val:
            sol3 = self.my_sol(row - 1, col + 1)
        return max(sol1, sol2, sol3) + 1

    def maxMoves(self, grid: List[List[int]]) -> int:
        self.grid = grid
        ans = 0
        for i in range(len(self.grid)):
            # print(i)
            ans = max(self.my_sol(i, 0), ans)
        return ans - 1


data = [[3,2,4],[2,1,9],[1,1,7]]
r = Solution().maxMoves(data)
print(r)