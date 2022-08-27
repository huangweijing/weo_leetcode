from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if prices is None or len(prices) == 0 or k == 0:
            return 0

        k = k + 1

        buy = [[0] * k for i in range(len(prices))]
        sell = [[0] * k for i in range(len(prices))]
        buy_hold = [[0] * k for i in range(len(prices))]
        sell_hold = [[0] * k for i in range(len(prices))]
        max_profit = [[0] * k for i in range(len(prices))]

        for i in range(k):
            buy[0][i] = -10000000000000
            sell[0][i] = -10000000000000
            buy_hold[0][i] = -10000000000000
        buy[0][1] = -prices[0]

        max_profit = [0] * k
        for i in range(1, len(prices)):
            buy[i][0] = -10000000000000
            sell[i][0] = -10000000000000
            buy_hold[i][0] = -10000000000000
            sell_hold[i][0] = sell_hold[i - 1][0]
            max_profit = [0] * k
            for j in range(1, k):
                buy[i][j] = max(sell[i - 1][j - 1], sell_hold[i - 1][j - 1]) - prices[i]
                sell[i][j] = max(buy_hold[i - 1][j], buy[i - 1][j]) + prices[i]
                buy_hold[i][j] = max(buy_hold[i - 1][j], buy[i - 1][j])
                sell_hold[i][j] = max(sell_hold[i - 1][j], sell[i - 1][j])
                max_profit[j] = max(buy[i][j], sell[i][j], buy_hold[i][j], sell_hold[i][j])
            # print(max_profit)

        # print(buy, sell, buy_hold, sell_hold)
        return max(max_profit)

data_k = 2
data = [1,101,2,202,1,301]
r = Solution().maxProfit(data_k, data)
print(r)
