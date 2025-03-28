from typing import List
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.cnt = Counter()

    def get_cost(self, line: int) -> int:
        ret = 0
        for key, val in self.cnt.items():
            ret += abs(key - line) * val
        return ret

    def minOperations(self, grid: List[List[int]], x: int) -> int:
        self.cnt = Counter()
        mod = -1
        max_val = -1
        min_val = 10e9
        for row in grid:
            for val in row:
                if mod == -1:
                    mod = val % x
                elif mod != val % x:
                    return -1
                self.cnt[(val - val % x) // x] += 1
                max_val = max(max_val, (val - val % x) // x)
                min_val = min(min_val, (val - val % x) // x)
        left, right = min_val, max_val
        mid = left + right >> 1
        # print(self.cnt)
        while left <= right:
            cost_min = self.get_cost(mid - 1)
            cost = self.get_cost(mid)
            cost_plus = self.get_cost(mid + 1)
            # print(cost_min, cost, cost_plus)
            if cost_min >= cost and cost_plus >= cost:
                return cost
            elif cost_min <= cost <= cost_plus:
                right = mid
            elif cost_min >= cost >= cost_plus:
                left = mid + 1
            mid = left + right >> 1
            # print(left, right)
        return mid

data = [
    [[503,503,9852,9852,9852,9852,9852,503,9852,503],[9852,9852,9852,9852,503,9852,9852,9852,503,503],[503,503,9852,9852,9852,9852,9852,503,9852,9852],[9852,9852,503,9852,503,9852,503,503,9852,503],[503,503,503,503,9852,9852,503,503,503,503],[9852,503,9852,9852,9852,9852,503,9852,9852,503],[503,503,9852,9852,503,503,9852,503,9852,9852],[503,9852,503,9852,503,503,503,503,503,503],[503,503,9852,9852,9852,503,503,503,9852,9852],[9852,9852,9852,9852,503,503,503,503,503,9852]]
    , 9349
]
r = Solution().minOperations(*data)
print(r)