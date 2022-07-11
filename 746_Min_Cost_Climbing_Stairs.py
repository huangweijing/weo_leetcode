from typing import List

class Solution:
    def __init__(self):
        self.dp = []

    def climb_stair(self, cost: List[int], pos: int) -> int:
        # print(cost, pos)
        if pos == 0 or pos == 1:
            return cost[pos]
        if self.dp[pos] is not None:
            return self.dp[pos]
        c1 = self.climb_stair(cost, pos - 1)
        c2 = self.climb_stair(cost, pos - 2)
        if c1 < c2:
            total_cost = c1 + cost[pos]
        else:
            total_cost = c2 + cost[pos]
        self.dp[pos] = total_cost
        # print(self.dp)
        return total_cost


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp = [None] * len(cost)
        c1 = self.climb_stair(cost, len(cost) - 1)
        c2 = self.climb_stair(cost, len(cost) - 2)
        if c1 < c2:
            return c1
        else:
            return c2

data = [10,15,20]
r = Solution().minCostClimbingStairs(data)
print(r)
