from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cost_dp = [0] * 3
        for num in nums:
            new_cost_dp = [-1] * 3
            if num == 1:
                new_cost_dp[0] = cost_dp[0]
                new_cost_dp[1] = min(cost_dp[0], cost_dp[1]) + 1
                new_cost_dp[2] = min(cost_dp) + 1
            elif num == 2:
                new_cost_dp[0] = cost_dp[0] + 1
                new_cost_dp[1] = min(cost_dp[0], cost_dp[1])
                new_cost_dp[2] = min(cost_dp) + 1
            else:
                new_cost_dp[0] = cost_dp[0] + 1
                new_cost_dp[1] = min(cost_dp[0], cost_dp[1]) + 1
                new_cost_dp[2] = min(cost_dp)
            cost_dp = new_cost_dp
        return min(cost_dp)

