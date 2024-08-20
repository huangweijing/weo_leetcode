from typing import List
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.piles = []
        self.prefix_sum = []

    def sum_range(self, i: int, j: int) -> int:
        if j + 1 >= len(self.prefix_sum) or i >= len(self.prefix_sum):
            return 0
        return self.prefix_sum[j + 1] - self.prefix_sum[i]

    @cache
    def calc_best(self, m: int, start: int) -> tuple[int, int]:
        if start >= len(self.piles):
            return (0, 0)
        ret = (0, 0)
        max_me = 0
        res_range = []
        for i in range(1, 2 * m + 1):
            if start + i > len(self.piles):
                break
            next_op, next_me = self.calc_best(max(i, m), start + i)
            curr_me = self.sum_range(start, start + i - 1)
            if curr_me + next_me > max_me:
                ret = (curr_me + next_me, next_op)
                max_me = curr_me + next_me
                res_range = self.piles[start: start + i]
        #     print(f"({m}, {start}) check range={res_range} -> score={ret}, ")
        # print(f"solution of ({m}, {start}) is score={ret}, range={res_range}")
        return ret

    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        ps = 0
        self.prefix_sum = [0]
        for pile in self.piles:
            ps += pile
            self.prefix_sum.append(ps)
        return self.calc_best(1, 0)[0]
        

data = [77,12,64,35,28,4,87,21,20]
# print("sum_data", sum(data))
r = Solution().stoneGameII(data)
print(r)