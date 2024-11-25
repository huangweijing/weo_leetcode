from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]],
                  travelScore: List[List[int]]) -> int:
        dp = [0] * n
        for i in range(k):
            new_dp = [0] * n
            for j in range(n):
                for k in range(n):
                    if j == k:
                        new_dp[k] = max(new_dp[k], dp[j] + stayScore[i][k])
                    else:
                        new_dp[k] = max(new_dp[k], dp[j] + travelScore[j][k])
            dp = new_dp
        return max(dp)

        