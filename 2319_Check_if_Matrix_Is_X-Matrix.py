from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if ((i == j or i == len(row) - 1 - j) and val == 0) \
                        or (i != j and i != len(row) - 1 - j and val != 0):
                    return False
        return True

grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
r = Solution().checkXMatrix(grid)
print(r)