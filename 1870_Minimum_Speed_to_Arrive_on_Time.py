from typing import List
import math


class Solution:
    def __init__(self):
        self.dist = []
        self.hour = 0

    def speed_okay(self, speed: int) -> bool:
        hour_taken = 0
        res = True
        for d in self.dist[:-1]:
            hour_taken += math.ceil(d / speed)
            if hour_taken > self.hour:
                res = False
                break
        hour_taken += self.dist[-1] / speed
        if hour_taken > self.hour:
            res = False
        # print(f"speed={speed}, hour_taken={hour_taken}, self.hour={self.hour}, res={res}")
        return res


    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        self.hour = hour
        self.dist = dist
        left, right = 1, 10 ** 7
        mid = right >> 1
        while left <= right:
            func1_res = self.speed_okay(mid)
            func2_res = self.speed_okay(mid + 1)
            if not func1_res and func2_res:
                return mid + 1
            elif func1_res and func2_res:
                right = mid - 1
            else:
                left = mid + 1
            mid = left + right >> 1
        if mid < 1:
            return 1
        else:
            return -1


data = [
    [1,1,100000]
    , 2.01
]
r = Solution().minSpeedOnTime(*data)
print(r)