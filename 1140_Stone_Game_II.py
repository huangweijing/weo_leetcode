from typing import List
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.best = [[0]]
        self.piles = []
        self.prefix_sum = []

    @cache
    def calc_best(self, m: int, start: int) -> int:
        if start == len(self.piles) - 1:
            return self.piles[-1]
        ret = 0
        for i in range(1, min(len(self.piles), m * 2 + 1)):
            if start + i >= len(self.piles):
                break
            val = -self.calc_best(i, start + i + 1) + self.prefix_sum[start + i + 1] \
                - self.prefix_sum[start]
            ret = max(ret, val)
        return ret


    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        ps = 0
        self.prefix_sum = [0]
        for pile in self.piles:
            ps += pile
            self.prefix_sum.append(ps)
        return self.calc_best(1, 0)
        

data = [1,2,3,4,5,100]
r = Solution().stoneGameII(data)
print(r)