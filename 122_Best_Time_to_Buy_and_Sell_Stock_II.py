from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                max_profit += profit
        return max_profit

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * len(prices)
        sell = [0] * len(prices)
        buy_hold = [0] * len(prices)
        sell_hold = [0] * len(prices)
        buy[0] = -prices[0]
        sell[0] = - (10 ** 4)
        buy_hold[0] = - (10 ** 4)
        sell_hold[0] = 0
        max_profit = 0
        for i in range(1, len(prices)):
            buy[i] = max(sell_hold[i - 1], sell[i - 1]) - prices[i]
            sell[i] = max(buy_hold[i - 1], buy[i - 1]) + prices[i]
            buy_hold[i] = max(buy_hold[i - 1], buy[i - 1])
            sell_hold[i] = max(sell[i - 1], sell_hold[i - 1])
            max_profit = max(buy[i], sell[i], buy_hold[i], sell_hold[i])
            # print(max_profit)
        return max_profit

r = Solution2().maxProfit([7,1,5,3,6,4])
print(r)

