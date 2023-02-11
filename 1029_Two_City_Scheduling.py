import math
from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.costs = []

    @cache
    def my_sol(self, n1: int, n2: int) -> int:
        if n1 == n2 == 0:
            return 0
        if n1 < 0 or n2 < 0:
            return math.inf
        cost = self.costs[n1 + n2 - 1]
        # go to city1
        total_cost1 = self.my_sol(n1 - 1, n2) + cost[0]
        # go to city2
        total_cost2 = self.my_sol(n1, n2 - 1) + cost[1]
        return min(total_cost1, total_cost2)

    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        self.costs = costs
        return self.my_sol(len(costs) >> 1, len(costs) >> 1)

data = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
r = Solution().twoCitySchedCost(data)
print(r)
