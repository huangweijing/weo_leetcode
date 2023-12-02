from typing import List
import math


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return prices[0]
        dp = [[math.inf, math.inf] for _ in range(len(prices) + 1)]
        dp[0] = [0, 0]
        for i, price in enumerate(prices, start=1):
            dp[i][1] = min(dp[i - 1][0], dp[i][0]) + price
            for j in range(i + 1, min(i + i + 1, len(prices) + 1)):
                dp[j][0] = min(dp[i][1], dp[j][0])
        # print(dp)
        return min(dp[-1][0], dp[-1][1])

data = [1,10,1,1]
r = Solution().minimumCoins(data)
print(r)