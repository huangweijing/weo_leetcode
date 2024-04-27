from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []
        ans = prices.copy()
        for i, price in enumerate(prices):
            while len(stk) > 0 and stk[-1][1] >= price:
                pos = stk.pop()
                ans[pos[0]] = pos[1] - price
            stk.append([i, price])
        return ans


data = [8,4,6,2,3]
r = Solution().finalPrices(data)
print(r)


