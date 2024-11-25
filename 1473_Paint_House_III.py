from typing import List
import math
from functools import cache


class Solution:
    def __init__(self) -> None:
        self.houses = []
        self.cost = []
        self.target = 0

    @cache
    def my_sol(self, color: int, idx: int, target: int) -> int:
        # if len(self.houses) - idx
        ret = math.inf
        if len(self.houses) - idx - 1 < target:
            return ret
        # paint different color
        for i, color_cost in enumerate(self.cost[idx]):
            new_target = target
            if i != color:
                new_target = target + 1
            if self.houses[idx] == i:
                ret = min(ret, self.my_sol(i, idx + 1, new_target))
            else:
                ret = min(ret, color_cost + self.my_sol(i, idx + 1, new_target))
        return ret

    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        self.houses, self.cost, self.target = houses, cost, target
        ans = math.inf
        for i in range(n):
            ans = min(self.my_sol(i, 0, target), ans)
        return ans
    

data = [
    [0,0,0,0,0]
    , [[1,10],[10,1],[10,1],[1,10],[5,1]]
    , 5
    , 2
    , 3
]
r = Solution().minCost(*data)
print(r)

        