from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.dp = [-2] * (10 ** 4 + 1)
        self.dp[0] = 0

    def coinChange(self, coins: List[int], amount: int) -> int:
        if self.dp[amount] != -2:
            return self.dp[amount]
        if amount < 0:
            return -1
        min_cnt = amount + 1
        for coin in coins:
            if amount - coin < 0:
                continue
            cnt = self.coinChange(coins, amount - coin)
            if cnt != -1:
                min_cnt = min(min_cnt, cnt + 1)

        if min_cnt == amount + 1:
            min_cnt = -1
        self.dp[amount] = min_cnt
        # print(self.dp)
        return min_cnt

data_coin = [1, 2, 5]
data_amount = 11
r = Solution().coinChange(data_coin, data_amount)
print(r)