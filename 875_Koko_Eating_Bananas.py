from typing import List
import math

class Solution:
    def __init__(self):
        self.piles = []
        self.h = 0

    def need_hour(self, speed: int) -> int:
        if speed == 0:
            return math.inf
        h = 0
        for pile in self.piles:
            h += math.ceil(pile / speed)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        self.piles = piles
        self.h = h
        left, right = 1, (piles[-1] * len(piles) * 100) // h
        while left <= right:
            mid = left + right >> 1
            test_hour = self.need_hour(mid)
            # print(left, mid, right, test_hour)
            if test_hour > h:
                left = mid + 1
            else:
                if self.need_hour(mid - 1) > h:
                    return mid
                else:
                    right = mid - 1
        return mid

data = [
    [1]
    , 5
]
r = Solution().minEatingSpeed(* data)
print(r)
