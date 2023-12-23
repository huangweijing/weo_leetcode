from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * k
              for _ in grid[0]]
              for _ in grid]
        dp[0][0][grid[0][0] % k] = 1
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if i > 0:
                    for mod_val in range(len(dp[i - 1][j])):
                        dp[i][j][(mod_val + val) % k] += dp[i - 1][j][mod_val]
                        dp[i][j][(mod_val + val) % k] %= mod
                if j > 0:
                    for mod_val in range(len(dp[i][j - 1])):
                        dp[i][j][(mod_val + val) % k] += dp[i][j - 1][mod_val]
                        dp[i][j][(mod_val + val) % k] %= mod
        return dp[-1][-1][0]


data = [
    [[5,2,4],[3,0,5],[0,7,2]]
    , 3
]
r = Solution().numberOfPaths(* data)
print(r)