from typing import List
import math


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [0] * 3
        dp[0], dp[2] = 1, 1
        for o in obstacles:
            new_dp = [0] * 3
            if o == 0:
                new_dp[0] = min(dp[0], dp[1] + 1, dp[2] + 1)
                new_dp[1] = min(dp[1], dp[0] + 1, dp[2] + 1)
                new_dp[2] = min(dp[2], dp[0] + 1, dp[1] + 1)
            elif o == 1:
                new_dp[0] = math.inf
                new_dp[1] = min(dp[1], dp[2] + 1)
                new_dp[2] = min(dp[2], dp[1] + 1)
            elif o == 2:
                new_dp[0] = min(dp[0], dp[2] + 1)
                new_dp[1] = math.inf
                new_dp[2] = min(dp[2], dp[0] + 1)
            elif o == 3:
                new_dp[0] = min(dp[0], dp[1] + 1)
                new_dp[1] = min(dp[1], dp[0] + 1)
                new_dp[2] = math.inf
            dp = new_dp
        return min(dp)


data = [0,1,2,3,0]
r = Solution().minSideJumps(data)
print(r)

