from typing import List, Any
import bisect


class Solution:
    def __init__(self):
        self.weights = []
        self.days = 0
        self.min_ship_weight = 0
        pass

    def check_ship_weight(self, ship_weight: int):
        idx = 0
        for i in range(self.days):
            new_ship_weight = ship_weight
            while idx < len(self.weights):
                if new_ship_weight < self.weights[idx]:
                    break
                new_ship_weight -= self.weights[idx]
                idx += 1
            if idx == len(self.weights):
                return True
        return False


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights, self.days = weights, days
        for weight in weights:
            self.min_ship_weight = max(self.min_ship_weight, weight)

        left, right = 1, len(weights) * self.min_ship_weight
        mid = left + right >> 1
        while left <= right:
            mid = left + right >> 1
            mid_1_res = self.check_ship_weight(mid - 1)
            mid_res = self.check_ship_weight(mid)
            if not mid_1_res and mid_res:
                return mid
            if not mid_res:
                left = mid + 1
            elif mid_1_res:
                right = mid - 1
        return mid

data = [
    [10,50,100,100,50,100,100,100]
]
r = Solution().shipWithinDays(*data, 5)
print(r)

