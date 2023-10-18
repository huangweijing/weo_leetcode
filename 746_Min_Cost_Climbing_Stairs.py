from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp2, dp1 = cost[0], cost[1]
        for i, c in enumerate(cost[2: ], start=2):
            dp = min(dp1, dp2) + cost[i]
            dp1, dp2 = dp, dp1
        return min(dp1, dp2)

data = [10,15,20]
r = Solution().minCostClimbingStairs(data)
print(r)
