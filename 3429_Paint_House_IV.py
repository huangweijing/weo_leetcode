from typing import List
import math


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        dp = [[math.inf] * 3 for _ in range(3)]
        left_idx, right_idx = n // 2 - 1, n // 2
        for i in range(3):
            for j in range(3):
                if i != j:
                    dp[i][j] = min(cost[left_idx][i] + cost[right_idx][j], dp[i][j])
        for i in range(1, n // 2):
            new_dp = [[math.inf] * 3 for _ in range(3)]
            left_idx = n // 2 - 1 - i
            right_idx = n // 2 + i
            for i in range(3):
                for j in range(3):
                    if i != j:
                        min_cost = math.inf
                        for k in range(3):
                            for l in range(3):
                                if i == k or j == l:
                                    continue
                                min_cost = min(min_cost, dp[k][l])
                                new_dp[i][j] = min(cost[left_idx][i] + cost[right_idx][j] + min_cost, new_dp[i][j])
            dp = new_dp
        return min([min(row) for row in dp])
        

data = [
    6
    , [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]
]
r = Solution().minCost(*data)
print(r)