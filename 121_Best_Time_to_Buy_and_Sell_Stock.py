from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_arr = []
        max_arr = []
        mi = 10 ** 5 + 1
        ma = 0
        idx = 0
        while idx < len(prices):
            num1 = prices[idx]
            num2 = prices[-idx - 1]
            if num1 < mi:
                mi = num1
            if num2 > ma:
                ma = num2
            # print(num2)
            min_arr.append(mi)
            max_arr.append(ma)
            idx += 1

        max_arr.reverse()
        # print(min_arr)
        # print(max_arr)
        idx = 0
        best_profit = 0
        while idx < len(prices):
            profit = max_arr[idx] - min_arr[idx]
            if profit > best_profit:
                best_profit = profit
            idx += 1
        return best_profit

data = [7,6,4,3,1]
sol = Solution()
r = sol.maxProfit(data)
print(r)
