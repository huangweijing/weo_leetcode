from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        left_dp = [[0] * len(grid[0]) for _ in grid]
        right_dp = [[0] * len(grid[0]) for _ in grid]
        up_dp = [[0] * len(grid[0]) for _ in grid]
        down_dp = [[0] * len(grid[0]) for _ in grid]
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    if j > 0:
                        left_dp[i][j] = left_dp[i][j - 1] + 1
                    else:
                        left_dp[i][j] = 1

                    if i > 0:
                        up_dp[i][j] = up_dp[i - 1][j] + 1
                    else:
                        up_dp[i][j] = 1

        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[i]))):
                if grid[i][j] == 1:
                    if j < len(grid[i]) - 1:
                        right_dp[i][j] = right_dp[i][j + 1] + 1
                    else:
                        right_dp[i][j] = 1
                    if i < len(grid) - 1:
                        down_dp[i][j] = down_dp[i + 1][j] + 1
                    else:
                        down_dp[i][j] = 1
        # print(left_dp, up_dp, right_dp, down_dp)
        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                v1 = min(right_dp[i][j], down_dp[i][j])
                if v1 > 0:
                    x = 0
                    while i + x < len(grid) and j + x < len(grid[0]) and x < v1:
                        v2 = min(left_dp[i + x][j + x], up_dp[i + x][j + x])
                        if min(v1, v2) > x:
                            ans = max(ans, x + 1)
                        x += 1
        return ans ** 2
    

data = [[1,1,0,0]]
r = Solution().largest1BorderedSquare(data)
print(r)
                        