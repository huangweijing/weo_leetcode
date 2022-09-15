import math
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = [-math.inf, 0]
        sell = [-math.inf, 0]
        hold = [-math.inf, 0]
        free = [0, 0]
        for price in prices:
            buy[1] = max(free[0], sell[0]) - price
            sell[1] = max(hold[0], buy[0]) + price - fee
            hold[1] = max(hold[0], buy[0])
            free[1] = max(free[0], sell[0])

            buy[0] = buy[1]
            sell[0] = sell[1]
            hold[0] = hold[1]
            free[0] = free[1]

            # print(f"price={price}, buy={buy[0]}, sell={sell[0]}, hold={hold[0]}, free={free[0]}")

        return max(buy[0], sell[0], hold[0], free[0])

data_prices = [1,3,7,5,10,3]
data_fee = 3
r = Solution().maxProfit(data_prices, data_fee)
print(r)