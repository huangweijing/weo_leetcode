from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                member = set[int]()
                is_magic = True
                col_sum = [0, 0, 0]
                for ri in range(3):
                    sum_row = 0
                    for ci in range(3):
                        sum_row += grid[i + ri][j + ci]
                        member.add(grid[i + ri][j + ci])
                        col_sum[ci] += grid[i + ri][j + ci]
                    if sum_row != 15:
                        is_magic = False
                if col_sum != [15, 15, 15]:
                    is_magic = False
                if member != set(range(1, 10)):
                    is_magic = False
                if is_magic:
                    ans += 1
        return ans
                    

        