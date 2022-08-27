from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy_hold = [0] * len(prices)
        sell_hold = [0] * len(prices)
        buy[0] = -prices[0]
        sell[0] = -10000
        buy_hold[0] = -10000
        last_day = len(prices) - 1
        for i in range(1, len(prices)):
            buy[i] = sell_hold[i - 1] - prices[i]
            sell[i] = max(buy_hold[i - 1], buy[i - 1]) + prices[i]
            buy_hold[i] = max(buy_hold[i - 1], buy[i - 1])
            sell_hold[i] = max(sell[i - 1], sell_hold[i - 1])
            # print(buy, sell, buy_hold, sell_hold, max(buy[i], sell[i], buy_hold[i], sell_hold[i]), sep="\n")
            # print()
        return max(buy[last_day], sell[last_day], buy_hold[last_day], sell_hold[last_day])

data = [6,1,3,2,4,7]
r = Solution().maxProfit(data)
print(r)
