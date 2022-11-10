from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_move, col_move = [0] * m, [0] * n
        ans = m * (1 << (n - 1))
        for i, row in enumerate(grid):
            if row[0] == 0:
                row_move[i] += 1

        for j in range(n):
            if j == 0:
                continue
            zero_cnt, one_cnt = 0, 0
            for i in range(m):
                if row_move[i] == 1:
                    if grid[i][j] == 0:
                        one_cnt += 1
                    else:
                        zero_cnt += 1
                else:
                    if grid[i][j] == 0:
                        zero_cnt += 1
                    else:
                        one_cnt += 1
            ans += max(zero_cnt, one_cnt) * (1 << (n - 1 - j))

        return ans

data = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
r = Solution().matrixScore(data)
print(r)


