from typing import List
import math


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ans = -math.inf
        dp = [[0] * len(grid[0]) for _ in grid]
        for i, row in enumerate(reversed(grid)):
            row_idx = len(dp) - 1 - i
            for j, val in enumerate(reversed(row)):
                col_idx = len(row) - 1 - j
                right_max, down_max = 0, 0
                if col_idx < len(row) - 1:
                    right_max = dp[row_idx][col_idx + 1]
                if row_idx < len(grid) - 1:
                    down_max = dp[row_idx + 1][col_idx]
                if row_idx < len(grid) - 1 or col_idx < len(row) - 1:
                    ans = max(ans, max(right_max, down_max) - val)
                dp[row_idx][col_idx] = max(right_max, down_max, val)
        # print(dp)
        return ans
        
data = [[10,5],[5,1]]
r = Solution().maxScore(data)
print(r)
