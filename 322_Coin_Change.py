from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.dp = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [-1] * (amount + 1)
        self.dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if self.dp[i - coin] == -1:
                    continue

                if self.dp[i] == -1:
                    self.dp[i] = self.dp[i - coin] + 1
                else:
                    self.dp[i] = min(self.dp[i - coin] + 1, self.dp[i])
        return self.dp[amount]

data_coin = [2]
data_amount = 3
r = Solution().coinChange(data_coin, data_amount)
print(r)