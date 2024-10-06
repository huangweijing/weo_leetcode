from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) <= 1:
            return 0
        stockPrices.sort()
        slopes = []
        for i, price in enumerate(stockPrices[1:], start=1):
            slope = [price[0] - stockPrices[i - 1][0], price[1] - stockPrices[i - 1][1]]
            slopes.append(slope)
        ans = 1
        for i in range(1, len(slopes)):
            if slopes[i][0] * slopes[i - 1][1] == slopes[i][1] * slopes[i - 1][0]:
                continue
            ans += 1
        return ans


data = [[3,4],[1,2],[7,8],[2,3]]
r = Solution().minimumLines(data)
print(r)

