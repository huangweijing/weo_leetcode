from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [[0, 0, 0] for i in range(len(prices))]
        sell = [[0, 0, 0] for i in range(len(prices))]
        buy_hold = [[0, 0, 0] for i in range(len(prices))]
        sell_hold = [[0, 0, 0] for i in range(len(prices))]
        max_profit = [0] * len(prices)

        buy[0][0] = -10000000000000
        buy[0][1] = -prices[0]
        buy[0][2] = -10000000000000
        sell[0][0] = -10000000000000
        sell[0][1] = -10000000000000
        sell[0][2] = -10000000000000
        buy_hold[0][0] = -10000000000000
        buy_hold[0][1] = -10000000000000
        buy_hold[0][2] = -10000000000000
        buy_hold[0][0] = 0
        buy_hold[0][1] = -10000000000000
        buy_hold[0][2] = -10000000000000

        for i in range(1, len(prices)):
            buy[i][0] = -10000000000000
            buy[i][1] = sell_hold[i - 1][0] - prices[i]
            buy[i][2] = max(sell[i - 1][1], sell_hold[i - 1][1]) - prices[i]
            sell[i][0] = -10000000000000
            sell[i][1] = max(buy_hold[i - 1][1], buy[i - 1][1]) + prices[i]
            sell[i][2] = max(buy_hold[i - 1][2], buy[i - 1][2]) + prices[i]
            buy_hold[i][0] = -10000000000000
            buy_hold[i][1] = max(buy_hold[i - 1][1], buy[i - 1][1])
            buy_hold[i][2] = max(buy_hold[i - 1][2], buy[i - 1][2])
            sell_hold[i][0] = sell_hold[i - 1][0]
            sell_hold[i][1] = max(sell_hold[i - 1][1], sell[i - 1][1])
            sell_hold[i][2] = max(sell_hold[i - 1][2], sell[i - 1][2])
            max_profit[i] = max(buy[i][1], buy[i][2], sell[i][1], sell[i][2]
                                , buy_hold[i][1], buy_hold[i][2], sell_hold[i][0]
                                , sell_hold[i][1], sell_hold[i][2])
            # print(max_profit)
        return max_profit[len(prices) - 1]

data = [1,101,2,202,1,301]
r = Solution().maxProfit(data)
print(r)
