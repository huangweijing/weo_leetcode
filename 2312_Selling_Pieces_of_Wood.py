from typing import List
from functools import cache
from collections import Counter


class Solution:

    def __init__(self) -> None:
        self.prices = []
        self.price_mat = Counter()

    @cache
    def max_price(self, m: int, n: int) -> int:
        # print(m, n)
        ret = 0
        ret = max(ret, self.price_mat[f"{m},{n}"])
        for i in range(1, (m >> 1) + 1):
            ret = max(ret, self.max_price(i, n) + self.max_price(m - i, n))
        for i in range(1, (n >> 1) + 1):
            ret = max(ret, self.max_price(m, i) + self.max_price(m, n - i))
        return ret

    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        for price in prices:
            self.price_mat[f"{price[0]},{price[1]}"] = max(self.price_mat[f"{price[0]},{price[1]}"], price[2])
        return self.max_price(m, n)
    

data = [
    3
    , 5
    , [[1,4,2],[2,2,7],[2,1,3]]
]
r = Solution().sellingWood(*data)
print(r)