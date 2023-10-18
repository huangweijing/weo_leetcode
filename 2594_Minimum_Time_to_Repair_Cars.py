from typing import List
from functools import cache
import math


class Solution:
    def __init__(self):
        self.ranks = []
        self.cars = 0

    @cache
    def can_handle(self, time: int) -> bool:
        res = 0
        for rank in self.ranks:
            res += int(math.sqrt(time / rank))
        return res >= self.cars

    def repairCars(self, ranks: List[int], cars: int) -> int:
        self.ranks, self.cars = ranks, cars
        left, right = 1, math.ceil(cars / len(ranks)) ** 2 * max(ranks)
        mid = left + right >> 1
        while left <= right:
            # print(mid)
            sol1 = self.can_handle(mid - 1)
            sol2 = self.can_handle(mid)
            if not sol1 and sol2:
                return mid
            elif not sol2:
                left = mid + 1
            elif sol1:
                right = mid - 1
            mid = left + right >> 1
        return mid

r = Solution().repairCars([4,2,3,1], 10)
print(r)