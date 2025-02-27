from typing import List
import math


class Solution:
    def __init__(self) -> None:
        self.nums = []
        self.threshold = 0

    def my_sol(self, div: int) -> bool:
        sum_val = 0
        for num in self.nums:
            sum_val += math.ceil(num / div)
            if sum_val > self.threshold:
                return False
        return True

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        self.nums = nums
        self.threshold = threshold
        left, right = 1, 100000000
        mid = left + right >> 1
        while 1 < mid < 100000000:
            s1 = self.my_sol(mid)
            s2 = self.my_sol(mid - 1)
            if s1 and not s2:
                return mid
            elif s1 and s2:
                right = mid - 1
            elif not s1 and not s2:
                left = mid + 1
            mid = left + right >> 1
        return mid


data = [
    [21212,10101,12121]
    , 1000000
]
r = Solution().smallestDivisor(*data)
print(r)