from typing import List
from collections import defaultdict
import datetime


class Solution:
    def __init__(self):
        self.t1 = datetime.datetime.now()
        self.grid1 = list[list[int]]()
        self.grid2 = list[list[int]]()

    def print_time(self):
        if True:
            print(datetime.datetime.now() - self.t1)

    def count_island(self, row: int, col: int):
        m, n = len(self.grid2), len(self.grid2[0])
        self.grid2[row][col] = 2
        if self.grid1[row][col] == 1:
            is_island = True
        else:
            is_island = False
        if row > 0 and self.grid2[row - 1][col] == 1:
            is_island &= self.count_island(row - 1, col)
        if row < m - 1 and self.grid2[row + 1][col] == 1:
            is_island &= self.count_island(row + 1, col)
        if col > 0 and self.grid2[row][col - 1] == 1:
            is_island &= self.count_island(row, col - 1)
        if col < n - 1 and self.grid2[row][col + 1] == 1:
            is_island &= self.count_island(row, col + 1)
        return is_island



    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.grid1 = grid1
        self.grid2 = grid2
        ans = 0
        m, n = len(grid2), len(grid2[0])
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    is_island = self.count_island(i, j)
                    ans += 1 if is_island else 0
        #             if is_island:
        #                 print(i, j)
        # print(self.grid2)
        return ans

data = [
    [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    , [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
]
r = Solution().countSubIslands(*data)
print(r)