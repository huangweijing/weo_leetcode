from typing import List
import bisect
from functools import cache

class Solution:
    def __init__(self):
        self.days, self.costs = [], []

    @cache
    def min_cost(self, idx: int):
        if idx < 0:
            return 0
        day = self.days[idx]
        # 1 day pass
        cost1 = self.min_cost(idx - 1) + self.costs[0]
        # 7 days pass
        if day - 6 > 0:
            new_idx = bisect.bisect_left(self.days, day - 6)
            cost7 = self.min_cost(new_idx - 1) + self.costs[1]
        else:
            cost7 = self.costs[1]
        # 30 days pass
        if day - 29 > self.days[0]:
            new_idx = bisect.bisect_left(self.days, day - 29)
            cost30 = self.min_cost(new_idx - 1) + self.costs[2]
        else:
            cost30 = self.costs[2]
        return min(cost1, cost7, cost30)

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.days, self.costs = days, costs
        return self.min_cost(len(days) - 1)

data = [
    [1,4,6,7,8,20]
    , [7,2,15]
]
r = Solution().mincostTickets(* data)
print(r)